import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)  # create_react_agent is a function which takes llm, prompt and return an Agent which is based on the ReAct algorithm
# AgentExecutor is the runtime of the agent, it is going to recieve the prompts and instructions on what to do and help finish the task
# successfully
from langchain import hub  # To import premade prompts by the community
from tools.tools import get_profile_url_tavily

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")
print(OPENAI_API_KEY)
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        temperature=0,
        model_name="gpt-4o-mini",
    )

    template = """
    Given the full name {name_of_person} I want you to get me a link of their Linkedin Profile page.
    Your answer should contain only a URL
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    """
    In langchain this is how you create a tool, If the agents decide to use the tool for any of its processing then it's 
    going to refer to the name as the name parameter given here and based on the description given it's going to decide whether to 
    use a certain tool or not. And after deciding it is going to execute the function provided in the tool for achieving the result required.
    """    
    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin Profile Page",
            func=get_profile_url_tavily,
            description="Useful for when you get the Linkedin Page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")  # react prompt from the Langchain cofounder Harrison chase

    # Here, we are defining what agent we want to use, what is the LLM that the agent has to use and which tools it has to use, also how to
    # parse the output we get, it is going to accept our ReAct Prompt (react_prompt or the custom one we can define) 
    agent = create_react_agent(
        llm=llm, 
        tools=tools_for_agent,
        prompt=react_prompt
    ) 

    """
    From the langchain documentation about Agent Exector: (https://python.langchain.com/v0.1/docs/modules/agents/concepts/)
    The agent executor is the runtime for an agent. This is what actually calls the agent, executes the actions it chooses, passes the action outputs back to the agent, and repeats. In pseudocode, this looks roughly like:

    next_action = agent.get_action(...)
    while next_action != AgentFinish:
    observation = run(next_action)
    next_action = agent.get_action(..., next_action, observation)
    return next_action
    """
    # Now, we have to provide the runtime for the agent to make it run in loops and do stuff for us using ReAct agent. This is going to be 
    # our final agent that we are going to be runnning. These tools are the ones will be invoked. (Pretty Confusing).

    agent_executor = AgentExecutor(
        api_key=LANGSMITH_API_KEY,
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    # This is pretty confusing, You can think about the create_react_agent as a recipe what we are sending to the LLm and getting back and 
    # parsing it and but the agentexecutor is going to be respomsible for orchestrating all these and calling those functions.
    # Clarification: It is pretty confusing, we are using tools in create_react_agent and also AgentExecutor. 
    # I get that in create_react_agent we are defining the tools to pass it into the react prompt template. And in the agent executor 
    # we are passing it so that it can use those tools and execute them if required.

    result = agent_executor.invoke(
        input={
            "input": prompt_template.format_prompt(name_of_person=name)
        }
    )

    linkedin_profile_url = result["output"]

    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = lookup(name="Vaishnava Samudrala")
    print(linkedin_url)  # If you want to run this file, run it from the Ice breaker Project Folder with 
    # `python -m Agents.linkedin_lookup_agent` command because if you directly run it, it's not going to consider tools and the API Keys

