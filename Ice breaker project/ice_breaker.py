import os
from typing import Tuple
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pprint import pprint
from third_parties.linkedin import scrape_linkedin_profile, LINKEDIN_PROFILE_URL  # API Call to third parties
from Agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from Agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets  # API Call to third parties
from output_parsers import Summary, summary_parser


def ice_break_with(name: str) -> Tuple[Summary, str]:
    """Takes name as input and finds the most relevant Linkedin Link for the name and scrapes it to find the information required"""
    linkedin_url = linkedin_lookup_agent(name=name)  # Tavily search for Linkedin Profile of the given name (Link)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=True
    )  # Making an API Call using ProxyCurl to get Linkedin Details of the link found in the previous step

    twitter_username = twitter_lookup_agent(name=name)  # Tavily search for Twitter Profile of the given name (Link)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)  # To get twitter profile of the user from the link found in the
    # previous step with the use of Twitter API (which is very very very limited for free users, so using mock=True always)

    summary_template = """
    Given the Linkedin information about a person from linkedin:\n {information},\n\n
    and twitter posts:\n {twitter_posts}\n\n
    I want you to create:
    1. a short summary
    2. two interesting facts about them

    Use both information from Linkedin and Twitter
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions
        },  # We use partial variables to assign a default value to a variable without assigning the value everytime we invoke the agent 
        # or llm
    )

    print(f"The Summary Prompt Template variable: {summary_prompt_template}")

    print(
        "\n======================================================================================\n"
    )

    llm = ChatOpenAI(
        temperature=0, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY1")
    )

    print(
        "\n======================================================================================\n"
    )

    chain = (
        summary_prompt_template | llm | summary_parser
    )  # This is LCEL, which is a way to write langchain chains. it can be
    # built using pipe operator which will be feeding the previous process output as the input to the next one 

    res: Summary = chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )  # Here we are giving a type hint to the final
    # variable because we output parse the llm output

    print(
        "\n======================================================================================\n"
    )

    pprint(
        f"Result is \n Type of final variable: {type(res)}\n Summary: {res.summary}\n Facts: {res.facts}"
    )  # To get only the response from the LLM without any metadat from the AI Message Object, we can use the content variable like shown 
    # here

    return res, linkedin_data.get("profile_pic_url")


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
