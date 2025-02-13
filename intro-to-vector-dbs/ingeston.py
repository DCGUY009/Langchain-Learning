import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()


PINECONE_VECTOR_INDEX = "medium-blogs-embeddings-index"



if __name__ == "__main__":
    print("Ingesting")




