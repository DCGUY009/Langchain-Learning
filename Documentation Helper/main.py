import streamlit as st
from backend.core import run_llm
from typing import Set

st.header("Langchain v3 Documentation Helper")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

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
        generated_response = run_llm(query=prompt)
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])  
        # we are converting to set to eliminate duplicate links

        formatted_response = f"{generated_response["result"]} \n\n {create_sources_string(sources)}"

        st.markdown(formatted_response) 
