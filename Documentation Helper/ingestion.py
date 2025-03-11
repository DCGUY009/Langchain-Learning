import os 
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadtheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_docs():
    loader = ReadtheDocsLoader("Langchain-docs/api.python.langchain.com/en/latest")

    raw_documents = loader.load()

    print(f"Loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)


    pass


if __name__=="__main__":
    ingest_docs()


