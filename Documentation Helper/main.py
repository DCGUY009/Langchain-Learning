import streamlit as st
from backend.core import run_llm
from typing import Set

st.header("Langchain v3 Documentation Helper")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_answers_history"] = []
    st.session_state["chat_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()

    print("*******************************")
    print(sources_list)
    print("*******************************")

    sources_string = "Sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Generating Response"):
        generated_response = run_llm(
            query=prompt,
            chat_history=st.session_state["chat_history"]
            )
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])  
        # we are converting to set to eliminate duplicate links

        formatted_response = f"{generated_response["result"]} \n\n {create_sources_string(sources)}"

        # st.markdown(formatted_response) 

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))

if st.session_state["chat_answers_history"]:
    for user_query, generated_response in zip(st.session_state["user_prompt_history"], st.session_state["chat_answers_history"]):
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(generated_response)
