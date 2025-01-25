import os 
import requests
from dotenv import load_dotenv

load_dotenv()


# Always define a function with type of inputs defined so that it is clear for you and for others who see it, also if you want to set default 
# values like `mock`` in this function
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):  
    """ Scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile.
    """
    
    