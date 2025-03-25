from dotenv import load_dotenv
import os 
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

INDEX_NAME = "langchain-doc-index"

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")
os.environ["LANGSMITH_PROJECT"] = "Documentation Helper"

def run_llm(query: str):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
        )
    docsearch = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings
    )
    chat = ChatOpenAI(
        model="gpt-4o-mini",
        verbose=True,
        temperature=0,
        api_key=OPENAI_API_KEY
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    stuff_documents_chain = create_stuff_documents_chain(
        chat,
        retrieval_qa_chat_prompt
    )

    qa = create_retrieval_chain(
        retriever=docsearch.as_retriever(),
        combine_docs_chain=stuff_documents_chain
    )  # So, here the combine_docs_chain is used to do post processing of the documents that are retrieved based on our needs
    # So, after the documents are retrieved, maybe we want to summarize them or maybe we want some filtering or maybe some 
    # keyword extraction to happen whatever we want to do for such things we are putting it in combine_docs_chain. So, this gives us 
    # the flexibility to plugin our own funcitonality for some post processing after retrieval. 
    # TO-DO: Play around with this to see how we can modify the documents.

    result = qa.invoke(input={
        "input": query
    })
    new_result = {
        "query": result["input"],
        "result": result["answer"],
        "source_documents": result["context"]
    }  # Not needed: changed just to follow the course
    return new_result

if __name__ == "__main__":
    res = run_llm(query="What is a Langchain chain?")
    print(res["answer"])

