import os 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")

if __name__ == "__main__":
    print("Vector Store in Memory")