
from openai import AsyncOpenAI
import os
# uv add python-dotenv
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_API_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key = gemini_API_key,
    base_url=base_url
)
MODEL = OpenAIChatCompletionsModel(model = "gemini-2.0-flash", openai_client = client)





