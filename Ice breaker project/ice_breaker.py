import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pprint import pprint
from third_parties.linkedin import scrape_linkedin_profile, LINKEDIN_PROFILE_URL


if __name__ == "__main__":
    print("Hello Langchain!")

    print(
        "\n======================================================================================\n"
    )

    load_dotenv()
    # print(os.getenv('OPENAI_API_KEY1'))

    summary_template = """
    Given the Linkedin information {information} about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    print(
        f"The Summary Prompt Template variable: {summary_prompt_template}"
    ) 

    print(
        "\n======================================================================================\n"
    )

    llm = ChatOpenAI(
        temperature=0, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY1")
    )

    # llm = ChatOllama(model="llama3")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=LINKEDIN_PROFILE_URL, mock=True)

    print(
        "\n======================================================================================\n"
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data})

    print(
        "\n======================================================================================\n"
    )

    pprint(
        f"Result is {res.content}"
    )  # To get only the response from the LLM without any metadat from the AI Message Object, we can use the content variable like shown here
    
     
