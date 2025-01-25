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

# Always define a function with type of inputs defined so that it is clear for you and for others who see it, also if you want to set default 
# values like `mock`` in this function
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):  
    """ Scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile.
    """

    