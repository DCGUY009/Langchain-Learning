from dotenv import load_dotenv
import os
from langchain.agents import tool
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI

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
        stop="\nObservation"  # This will tell hte llm to stop genmerating the text and to finish working once it's ouputted (\nObservation)
        # why do we need it? Because llm is not going to stop and it is going to hallucinate and guess one word after another and runs in
        # an infinite loop
    )

    




