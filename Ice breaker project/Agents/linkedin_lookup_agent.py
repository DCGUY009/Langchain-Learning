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

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        api_key=OPENAI_API_KEY
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
            func="?",
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

    # Now, we have to provide the runtime for the agent to make it run in loops and do stuff for us using ReAct agent. This is going to be 
    # our final agent that we are going to be runnning. These tools are the ones will be invoked. (Pretty Confusing).

    agent_executor = AgentExecutor(
        llm=llm,
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