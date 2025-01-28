import os
from dotenv import load_dotenv
import tweepy  # Twitter API
import requests  # For static files (GIST)
from pprint import pprint

load_dotenv()


twitter_client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_KEY_sECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_sECRET")
)


# At this time (i.e. 28th Jan 2025) Twitter API is not free because Elon musk implemented charges for it. So, we will be using 
# Eden Marco's GIST Files mostly with mock set to True. But the code will contain the logic for twitter API as well. There is a free version 
# but it is limited to 100 post and 500 writes per month in 1 environment. So, mostly this will work
def scrape_user_tweets(username, num_tweets=5, mock: bool=False):
    """
    Scrapes a Twitter user's original tweets (i.e. mpt retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (related to now), "text", and "url".
    """
    tweet_list = []

    if mock:
        # Temporary for now, I will create my own after getting a similar response
        # EDEN_TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/1675c4b1595ec0ddd8208544a4f915769465ed6a/eden-marco-tweets.json"
        SAMUDRALASANTHOSH_TWITTER_GIST = "https://gist.githubusercontent.com/DCGUY009/aea84135ed9d89f52683e971a2cd9c9a/raw/88bc968d6d425c3d339697520fcf116961704d6c/gistfile1.txt"

        tweets = requests.get(SAMUDRALASANTHOSH_TWITTER_GIST, timeout=5).json()

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )
        pprint(tweets)



    for tweet in tweets["data"]:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet["id"]}"
        tweet_list.append(tweet_dict)
    
    return tweet_list
        

if __name__ == "__main__":

    tweets = scrape_user_tweets(username="santoshsamudra3")
    print(tweets)