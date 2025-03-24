import os 
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader 
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pprint import pprint 


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small", 
    api_key=OPENAI_API_KEY
    )
PINECONE_INDEX = "langchain-doc-index"


def ingest_docs():
    loader = ReadTheDocsLoader("D:/Genai_projects/Langchain - Develop LLM powered applications - Udemy Course/Documentation Helper/Documentation Scraping v3/langchain-docs/api.python.langchain.com/en/latest")

    raw_documents = loader.load()

    # for document in raw_documents:
    #     pprint(f"{document}\n---------------------\n")

    print(f"Loaded {len(raw_documents)} documents")
    """
    So, the tokens that we send to the LLM matter, every llm has a context limit. For eg, gpt-4o-mini has 1,28,000 
    context (https://platform.openai.com/docs/models/gpt-4o-mini) window (input + output tokens) and in that for output it has 
    16,384 token limit (Now this value will increase as cost of gpu's become cheaper). So, for the context that you are sending 
    to the LLM, if you decide that you will be sending 4 or 5 documents and you have allocated 2000 tokens for the context. Then 
    you have to chunk the documents into 500 words each (1 token can be a word, a set of words or a few alphabets: it varies). I 
    guess this is one way but it doesn't consider everything into, so how you chunk and how many chunks you need in your context is 
    totally dependent on the use case you are solving.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)

    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace(
            "D:\\Genai_projects\\Langchain - Develop LLM powered applications - Udemy Course\\Documentation Helper\\Documentation Scraping v3\\langchain-docs", 
            "https:/")
        # Convert backslashes to forward slashes
        new_url = new_url.replace("\\", "/")
        doc.metadata.update({"source": new_url})
    


    for document in documents:
        pprint(f"{document}\n---------------------\n")
    
    print(f"Going to add {len(documents)} to Pinecone")

    # for doc in documents:
    #     print(f"Raw metadata source: {repr(doc.metadata['source'])}")


    PineconeVectorStore.from_documents(
        documents, embeddings, index_name=PINECONE_INDEX
    )

    print("*** Loading to Vector Store done ***")


if __name__=="__main__":
    ingest_docs()


