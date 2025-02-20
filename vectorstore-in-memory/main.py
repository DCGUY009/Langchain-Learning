import os 
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

if __name__ == "__main__":

    print("Vector Store in Memory")
    pdf_path = "ReAct Paper.pdf"

    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()  # THis will make around 30 documents if you debug and evaluate this expression you can see
    # but we need to have more control over the chunking so that we don't hit our token limit wiht the llm. So, we need to
    # chunk up the cocuments more. So, we use CharacterTextSplitter

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")

    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("faiss_index_react")

    my_vector_store = FAISS.load_local(
        "faiss_index_react", embeddings, allow_dangerous_deserialization=True
    )  # The flag allow_dangerous_deserialization=True is a safety measure introduced by LangChain to address security
    # risks associated with unpickling data. When loading a FAISS index using load_local(), we are deserializing a
    #  previously saved vector store, which involves unpickling. Since pickle files can execute arbitrary code if 
    # tampered with, this makes the process susceptible to deserialization attacks. For this reason, using
    #  allow_dangerous_deserialization=True is not recommended in production environments.

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(
        ChatOpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY
        ),
        retrieval_qa_chat_prompt
    )

    retrieval_chain = create_retrieval_chain(
        my_vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    res = retrieval_chain.invoke({"input": "Give me the core logic of ReAct"})

    print(res["answer"])


