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
    loader = ReadtheDocsLoader("./Documentation Scraping v3/latest/")

    raw_documents = loader.load()

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


    pass


if __name__=="__main__":
    ingest_docs()


