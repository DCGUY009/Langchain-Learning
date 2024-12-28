import os 
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ Scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile.
    """