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
    result = chain.invoke(input={})
    print(result.content)

    vectorstore = PineconeVectorStore(
        index_name=PINECONE_VECTOR_INDEX, embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")




