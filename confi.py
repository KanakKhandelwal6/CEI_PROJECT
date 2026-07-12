from dotenv import load_dotenv
import os 

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


owner = "fastapi"
repo = "fastapi"

BASE_URL = f"https://api.github.com/repos/{owner}/{repo}"