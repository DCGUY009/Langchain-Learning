import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pprint import pprint
from third_parties.linkedin import scrape_linkedin_profile, LINKEDIN_PROFILE_URL
from Agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from Agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets

def ice_break_with(name: str) -> str:
    """Takes name as input and finds the most relevant Linkedin Link for the name and scrapes it to find the information required"""
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)

    summary_template = """
    Given the Linkedin information about a person from linkedin  {information},
    and twitter posts {twitter_posts}.
    I want you to create:
    1. a short summary
    2. two interesting facts about them

    Use both information from Linkedin and Twitter
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"], template=summary_template
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

    print(
        "\n======================================================================================\n"
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})

    print(
        "\n======================================================================================\n"
    )

    pprint(
        f"Result is {res.content}"
    )  # To get only the response from the LLM without any metadat from the AI Message Object, we can use the content variable like shown here



if __name__ == "__main__":
    print("Ice Breaker Enter")

    print(
        "\n======================================================================================\n"
    )

    load_dotenv()
    # print(os.getenv('OPENAI_API_KEY1'))

    # llm = ChatOllama(model="llama3")
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=LINKEDIN_PROFILE_URL, mock=True)    

    ice_break_with(name="Vaishnava Samudrala")
     
