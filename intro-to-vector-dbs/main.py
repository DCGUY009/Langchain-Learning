import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore 

from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from ingeston import PINECONE_VECTOR_INDEX

"""
When we do RAG, what happens in the backend is that first we store our documents in a vector database.
Then, the query that is asked is converted into embeddings and sent to the vector dbs for finding out the relevant
vector and returning them to us in the form of the vectors converted into text and this whole thing (user query + context 
retrieved from vector store which are relevant to the user query) is sent to the LLM which will process it and give us 
the output.

In langchain, all this is done by create_stuff_documents_chain and create_retrieval_chain (not storing the text in 
vector db but retrieving the relevant ones to the query from vectordb and converting them into text)
"""

load_dotenv()

os.environ["LANGSMITH_PROJECT"] = "Medium Analyzer"

openai_api_key = os.getenv("OPENAI_API_KEY1")

if __name__ == "__main__":
    print("Retrieving")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=openai_api_key
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=openai_api_key
    )


    # Checking what would happen if we don't ground the response with the relevant context

    query = "What is Pinecone in Machine Learning"
    chain = PromptTemplate.from_template(template=query) | llm
    # result = chain.invoke(input={})
    # print(result.content)

    vectorstore = PineconeVectorStore(
        index_name=PINECONE_VECTOR_INDEX, embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")  # This is going to be the prompt that 
    # is sent to the llm after we retrive the relevant information
     

    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)  # This function output us a 
    # langchain chain, we plug it in the llm and we give it a retrieval qa prompt and this chain takes a list of documents
    #  and formats them all into a prompt, then passes that prompt to an LLM. It passes ALL documents, so you should make 
    # sure it fits within the context window of the LLM you are using. 

    retrieval_chain = create_retrieval_chain(
        retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain
    )  # So, before we stuff the documents into the prompt we send into the LLM, we need to get those documents 
    # from somewhere, right? For that this chain is used. So, the retriver argument here is to get the documents 
    # and then run the combine_doc_chain to stuff all those documents into the prompt

    # If we don't want to simply stuff all the documents and put it in the prompt but summarize each document first
    # and then send it to the LLM. We can also do that.

    result = retrieval_chain.invoke(input={"input": query})

    print(result)


    # Let's take a custom Prompt that we create and then do RAG on it
    template = """Use the following pieces of context to answer the question at the end. If you don't 
    know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum
    and keep the answer as concise as possible. Always say 'thanks for asking!' at the end of the answer.

    {context}

    Question: {question}

    Helpful Answer:"""  # Pretty similar to the retrieval-qa-chat prompt we pulled from the hub earlier. Just the 
    # instruction is different a little bit

    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": vectorstore.as_retriever() | format_docs, "question": RunnablePassThrough()},
        custom_rag_prompt |
        llm
    )  # Using LCEL











