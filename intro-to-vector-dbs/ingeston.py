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

    loader = TextLoader("mediumblog1.txt")
    document = loader.load()

    # print(f"Loader: {loader} and Type of Loader: {type(loader)}")
    # # Loader: <langchain_community.document_loaders.text.TextLoader object at 0x00000234CF96EB10> and 
    # # Type of Loader: <class 'langchain_community.document_loaders.text.TextLoader'>

    # print(f"Document: {document} and Type of Document: {type(document)}")  # Type of Document: <class 'list'>

    print("Splitting...")

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  # Character Text Splitter object is very complex. 
    # it can regex, it can suse different length functions to count the number of tokens that we are splitting it for, etc
    # General rule of thumb is to keep chunk_size small enough to fix the context window of the llm and we would be getting multiple chunks 
    # and also not too small that there is no sense of the text/ So, keeping it small enough but not too small will help because if we 
    # as humans read a chunk we have to make a meaning out of it. So, keeping the chunk_size too small wouldn't make any sense to the LLM 
    # and we wouldn't understand anaything from it. Chunk_overlap is used to overlap beweem the chunks, when we don't want to lose 
    # context between chunks - overlapping data is useful

    # It's important to split the text into chunks even when we are using llms with large context window such as Gemini with 1 million 
    # tokens. Because another rule of llm, is "Garbage In, Garbage Out". So, if we send a lot of garbage which is uneccessary the first thing
    # that will affect us is the cost and then the llm would throw garbage out as it got lot of uneccessary information
    texts = text_splitter.split_documents(documents=document)  # which recieves a list of documents and splits it accordingly as we want
    # So, when you split the document into chunks. Make sure you read the chunks and make sure it has semantic value
    # you can read them and adjust your chunk size accordingly until you think it makes sense.

    print(f"created {len(texts)} documents")

    print(f"Text splitter: {text_splitter}\nType of Text Splitter: {type(text_splitter)}")
    print(f"Text: {texts}\nType of Text: {type(texts)}")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=os.getenv("OPENAI_API_KEY1")
    )

    print("Ingesting")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=PINECONE_VECTOR_INDEX)








