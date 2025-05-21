
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables
# from .env file
# Load the environment variables from the .env file
# Set the OpenAI API key and endpoint URL

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"


# Initialize the OpenAI client
# Note: The OpenAI client is initialized with the API key and endpoint URL.

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of Lithuania?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message.content)

