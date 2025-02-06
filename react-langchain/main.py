from dotenv import load_dotenv
import os
from langchain.agents import Tool, tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from typing import Union, List
from langchain_core.agents import AgentAction, AgentFinish

load_dotenv()

"""
We can use tool decorator in langchain that will take a function and convert it into a Langchain tool.

The tool decorator is a langchain utility function that will take the function we define and create a langchain tool from it.  

It's going to plugin the name of the function, what it receives as arguments, what it returns in the description and populate it 
in the langchain tool class
"""


@tool
def get_text_length(text: str)-> int:
    """Returns the length of a text by characters"""  # Description is vv important as this is used by the LLM to decide whether it has to 
    # use this tool or not 
    print(f"get_text_length enter with {text=}")
    text = text.strip("'\n").strip(
        '"'
    )  # stripping away non alphabetic characters just in case

    return len(text)


def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool with {tool_name} not found")


if __name__ == "__main__":
    print("Hello ReAct Langchain")
    # print(os.getenv("OPENAI_API_KEY1"))
    # print(get_text_length(text="Samudrala Sri Vignan Santhosh"))  # When trying to invoke a langchain tool you can't directly call 
    # # it like this
    # print(get_text_length.invoke(input={"text": "Samudrala Sri Vignan Santhosh"}))  # You have to invoke it this way
    # # If you want to debug what is happening at a certain point in your code - You can put a breakpoint at a certain line 
    # # and then right click on that particular line and click on "Evaluate in debug console". If you don't run into any error on that line
    # # then you can see things like get_text_length.description, get_text_length.args etc
    # # Here, we are passing in as input dictionary which is cumbersome because langchain wants to keep everything structured for LCEL

    tools = [get_text_length]  # List of langchain tools to supply to the ReAct Agent

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools), tool_names=", ".join([t.name for t in tools])
    )  # Here we can't directly pass tools=tools as it is a Tool object from langchain and we need strings of the tools
    # along with their arguments and descriptions because llm only accepts string. So, we use an inbuilt function from langchain
    # which converts this objects into string so that it is easier to procesws. The render_text_Description jsut formats it nicely 
    # into a string and gives us with tool names and descriptions for all the tools present

    print(prompt)

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY, 
        stop="\nObservation"  # This will tell hte llm to stop genmerating the text and to finish working once it's ouputted (\nObservation)
        # why do we need it? Because llm is not going to stop and it is going to hallucinate and guess one word after another and runs in
        # an infinite loop
    )

    agent = {"input": lambda x: x["input"]} | prompt | llm  # Here, Lambda function to extract the 'input' value from a dictionary
    # Takes a dictionary as input and returns the value associated with the 'input' key. 
    # This is LCEL, the main reason it was created because people complained that all the chains and agents they were
    # not able to understand what is happening under the hood. So, LCEL was created which gives more clarity. It has many options/benefits 
    # such as parallel processing, batch, streaming etc. With the help of LCEL we can understand what is happening at each step and what is
    # the chronological order of the executions. The pipe operator takes the output of the left side and inputs it into the right side

    agent1 = prompt | llm  # It's working the same in both the cases even if I don't define a dictionary like done in "agent" variable above
    # It is only done to show that the input is extracted first and then it is passed into the prompt (Just to demonstrate LCEL)

    """
    So, essentially 'agent' and 'agent1' what they are doing is it is going to the point till where the llm decides which tool to use 
    and what is the tool input. Now, our job is to parse the Action and Action input to execute the tool and pass the result of the tool 
    to the llm back. So, to extract the Action and Action input we can use regex but langchain has already implemented this and the 
    output parser name is ReActSingleInputOutputParser 
    """
    agent2 = prompt | llm | ReActSingleInputOutputParser()

    res = agent.invoke({"input": "What is the length of 'Samudrala Sri Vignan Santhosh' in characters?"})  
    res1 = agent1.invoke({"input": "What is the length of 'Samudrala Sri Vignan Santhosh' in characters?"})


    agent_step: Union[AgentAction, AgentFinish] = agent2.invoke(
            {
            "input": "What is the length of 'Samudrala Sri Vignan Santhosh' in characters?"
            }
        )  # Here, ReActSingleInputOutputParser return either AgentAction or AgentFinish types, 
           # AgentAction represents a request to execute an action by an agent. The action consists of the name of the tool to execute and 
           # the input to pass to the tool. The log is used to pass along extra information about the action. 
           # AgentFinish gives Final return value of an ActionAgent. Agents return an AgentFinish when they have reached a stopping condition

    print(f"With an input dictionary with lambda function before prompt in LCEL: {res}")
    print(f"Without an input dictionary with lambda function before prompt in LCEL: {res1}")
    print(f"Without output parser to parse Action and Ction input: {agent_step}")

    if isinstance(agent_step, AgentAction):
        tool_name = agent_step.tool
        tool_to_use = find_tool_by_name(tools, tool_name)
        tool_input = agent_step.tool_input

        observation = tool_to_use.func(str(tool_input))  # Here we know that the tool_input is going to be string that is why we are passing it
        # this way, but langchain has a more robust implementation covering all types

        print(f"Observation: {observation}")







    




