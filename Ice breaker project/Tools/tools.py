from langchain_community.tools.tavily_search import TavilySearchResults

# Tavily is a search API highly optimized for GenAI Workloads, it has a nice integration with Langchain
# It has the capability to search in Google, bing etc. But also, has the capability to figure out what to do based on the user query


# TavilySearchResults object implements the Tavily Search API Logic in the backend by Langchain
def get_profile_url_tavily(search: str):
    """Searches for Linkedin or Twitter Profile Page"""
    search_web = TavilySearchResults()
    res = search_web.run(
        f"{search}"
    )  # When we invoke it with the query, it is going to implement the tavily logic in the backend
    # and give us the result
    return res
