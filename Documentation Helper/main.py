import streamlit as st
from backend.core import run_llm
from typing import Set

# Configure the page
st.set_page_config(
    page_title="Langchain Documentation Helper",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        padding: 2rem 0;
        font-size: 2.5rem;
    }
    .stTextInput > div > div > input {
        background-color: #2D2D2D;
        color: white;
        border: 1px solid #565869;
        padding: 15px;
        border-radius: 10px;
    }
    .stChatInput > div > input {
        background-color: #2D2D2D;
        border: 1px solid #565869;
        border-radius: 10px;
        padding: 10px 15px;
    }
    .stSpinner > div > div {
        border-color: #565869 !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #1E1E1E;
        width: 300px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Sidebar content
with st.sidebar:
    st.title("🤖 AI Documentation Helper")
    st.markdown("""
    Welcome to the Langchain Documentation Helper! 
    
    This AI-powered assistant helps you:
    
    📚 Find relevant documentation
    💡 Answer technical questions
    🔍 Explore Langchain features
    🛠️ Solve implementation issues
    
    Just ask your question in the chat below!
    
    ---
    
    **How it works:**
    1. Ask any question about Langchain
    2. AI searches through documentation
    3. Get accurate, sourced answers
    
    ---
    
    Made with ❤️ using:
    - Langchain
    - Streamlit
    - OpenAI
    """)

# Function to create sources string
def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "Sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string

# Main interface
st.markdown('<h1 class="main-title">Langchain Documentation Helper</h1>', unsafe_allow_html=True)

# Display chat messages
for user_query, generated_response in zip(
    st.session_state["user_prompt_history"],
    st.session_state["chat_answers_history"]
):
    st.chat_message("user").write(user_query)
    st.chat_message("assistant").write(generated_response)

# Chat input - always at the bottom
prompt = st.chat_input("Ask anything about Langchain...")

# Handle prompt
if prompt:
    # Add user message to chat
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
    # Generate response
        with st.spinner("🤔 Searching documentation..."):
            generated_response = run_llm(
                query=prompt,
                chat_history=st.session_state["chat_history"]
            )
            sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])
            formatted_response = f"{generated_response['result']} \n\n {create_sources_string(sources)}"
            
            # Update session state
            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answers_history"].append(formatted_response)
            st.session_state["chat_history"].append(("human", prompt))
            st.session_state["chat_history"].append(("ai", generated_response["result"]))
            
            # Display assistant response
            st.write(formatted_response)
