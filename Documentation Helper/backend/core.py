from dotenv import load_dotenv
import os 
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from typing import List, Dict, Any

INDEX_NAME = "langchain-doc-index"

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")
os.environ["LANGSMITH_PROJECT"] = "Documentation Helper"

def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
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

    # Ok, for making sure that we are answering follow up questions better we need to rephrase the prompt and create a retriever for 
    # this as well
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")

    # Langchain created a history to take this new question 
    history_aware_retriever = create_history_aware_retriever(
        llm=chat,
        retriever=docsearch.as_retriever(),
        prompt=rephrase_prompt
    )  # So, here history aware retriever logic is basically a conditional logic implemented again in langchain by something called
    # as RunnableBranch: What the RunnabelBranch logic is is that it is going to choose a branch based on a condition. Now, in history
    # aware retriever there are 2 chains. One chain consists of our original retriever where we send our user prompt to the vector
    # db to get the relevant context directly (So, every new user query is sent to the vector db without any consideration for the 
    # past history). Now, what history aware retirver does is it has this condition where first it checks whether the chat_history key
    # is empty or not. Now, if it is empty then it is going to run the first chain we discussed. Now, if it is false what it is going 
    # to do is take the rephrase prompt the one we pulled from the langchain hub and the prompt is structured such that based on the 
    # current chat history, user question it will rephrase the question. Now, this rephrased question is extracted using StrOutputParser 4
    # and then passed in to the retriever to retrieve relevant context with the rephrased question. We are just using this so it would be 
    # helpful to us when there is a history.

    # qa = create_retrieval_chain(
    #     retriever=docsearch.as_retriever(),
    #     combine_docs_chain=stuff_documents_chain
    # )  # So, here the combine_docs_chain is used to do post processing of the documents that are retrieved based on our needs
    # # So, after the documents are retrieved, maybe we want to summarize them or maybe we want some filtering or maybe some 
    # # keyword extraction to happen whatever we want to do for such things we are putting it in combine_docs_chain. So, this gives us 
    # # the flexibility to plugin our own funcitonality for some post processing after retrieval. 
    # # TO-DO: Play around with this to see how we can modify the documents.

    # Replacing the retriever in qa with history aware retriever
    qa = create_retrieval_chain(
        retriever=history_aware_retriever,
        combine_docs_chain=stuff_documents_chain
    )  # So, here based on chat_history being empty or not, the history aware retriever might choose 2 different chains 
    # where in one chain if chat_history is empty then the user prompt is directly sent to the retriever to retrieve the context.
    # And if chat_history is not empty, then the rephrase prompt is used and then the user original question is rephrased considering
    # the chat_history and the relevant context is retrieved. Now, whatever way the context is retrieved (We just want the most 
    # relevant context) it is passed again to the retrieval_qa_chat_prompt with the system prompt + chat_history + context + user_input
    # (the original one). 

    result = qa.invoke(input={
        "input": query,
        "chat_history": chat_history
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

