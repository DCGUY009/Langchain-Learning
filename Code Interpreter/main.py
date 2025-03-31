import os
from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")


def main():
    print("Start...")

    instructions = """You are an agent designed """


if __name__ == "__main__":
    main()