import os 
import requests
from dotenv import load_dotenv

load_dotenv()
"""
For this, we went to Proxycurl API, use the Person Lookup Profile Endpoint. Because we only get few free credits we are saving 
the API Response of a profile after querying it (I did using Postman) we are saving it in gist.github.com and using the raw link 
to make HTTP Requests to it emulating something similar to an API Call. Also attaching the json file here for reference.

Link: https://gist.githubusercontent.com/DCGUY009/16175ccc5daa5fa1a19b15ce9fba8044/raw/149bccd37bc0e359d60193ecc9074278c10d8161/gistfile1.txt
"""

LINKEDIN_PROFILE_URL = "https://gist.githubusercontent.com/DCGUY009/16175ccc5daa5fa1a19b15ce9fba8044/raw/149bccd37bc0e359d60193ecc9074278c10d8161/gistfile1.txt"
PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")

# Always define a function with type of inputs defined so that it is clear for you and for others who see it, also if you want to set default 
# values like `mock`` in this function
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):  
    """ Scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile.
    """

    # If we want to use the mock file created in gist.github.com, we need to mock to true and if the mock is false, we make an API call
    # to the ProxyCurl API with the given Linkedin URL 
    if mock:
        linkedin_profile_url = LINKEDIN_PROFILE_URL
        response = requests.get(
            linkedin_profile_url,
            timeout = 10
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        headers = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=headers,
            timeout=10
        )
    
    data = response.json()  # If the user data contains a profile picture URL, it has a TTl (Tiem to Load) of 1 hour. After 1 hour, 
    # we cannot access the profile picture through the link. So, it is best if you save it somewhere in a storage

    return data
        


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/samudralasanthosh/",
            mock=True
        )
    )
    