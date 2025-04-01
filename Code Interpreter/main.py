import os
from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool, PythonAstREPLTool  # So all the experimental features which are not safe in production are 
# all part of this separate library in langchain. PythonREPLTool runs your python scripts in the interpreter and is very dangerous 
# to run in production environments. Hence, these type of tools are placed in langchain_experimental
from langchain_experimental.agents.agent_toolkits import create_csv_agent


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

python_repl_tool = PythonREPLTool()
python_ast_repl_tool = PythonAstREPLTool()


def main():
    print("Start...")

    instructions = """You are an agent designed to write and execute python code to answer questions.
    You ahave access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return 'I don't know' as the answer/ 
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")  # This is the modified react prompt with the instructions variable in it
    """
    The React Prompt is (Here the chat history is used to store the earlier messages and agent scratchpad is to store the internal
    reasoning done by the agent):
    
    {instructions}

    TOOLS:
    ------

    You have access to the following tools:

    {tools}

    To use a tool, please use the following format:

    ```
    Thought: Do I need to use a tool? Yes
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ```

    When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

    ```
    Thought: Do I need to use a tool? No
    Final Answer: [your response here]
    ```

    Begin!

    Previous conversation history:
    {chat_history}

    New input: {input}
    {agent_scratchpad}
    """

    prompt = base_prompt.partial(instructions=instructions)

    tools = [python_repl_tool]

    agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY
        ),
        tools=tools
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    # agent_executor.invoke(
    #     input={
    #         "input": """Generate and save in current working directory 15 QRCodes that point to 
    #         https://www.linkedin.com/in/samudralasanthosh/. You have qrcode package installed already."""
    #     }
    # )

    csv_agent = create_csv_agent(
        llm = ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY
        ),
        path="./Data/episode_info.csv",
        verbose=True,
        allow_dangerous_code=True, 
        agent_type="zero-shot-react-description"
    )

    csv_agent.invoke(
        input={
            "input": "How many columns are there in file episode_info.csv"
        }
    )

    csv_agent.invoke(
        input={
            "input": "print the seasons by ascending order of the number of episodes they have"
        }
    )


if __name__ == "__main__":
    main()