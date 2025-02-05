from dotenv import load_dotenv
import os
from langchain.agents import tool

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
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct Langchain")
    # print(os.getenv("OPENAI_API_KEY1"))
    # print(get_text_length(text="Samudrala Sri Vignan Santhosh"))  # When trying to invoke a langchain tool you can't directly call 
    # # it like this
    print(get_text_length.invoke(input={"text": "Samudrala Sri Vignan Santhosh"}))  # You have to invoke it this way
    # If you want to debug what is happening at a certain point in your code - You can put a breakpoint at a certain line 
    # and then right click on that particular line and click on "Evaluate in debug console". If you don't run into any error on that line
    # then you can see things
