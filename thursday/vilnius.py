
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables
# from .env file
# Load the environment variables from the .env file
# Set the OpenAI API key and endpoint URL

token = os.getenv("API_KEY")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# Uploading the context from 'vilnius.txt'
with open('vilnius.txt', 'r', encoding='utf-8') as file:
    context = file.read()

# Initialize the OpenAI client
# Note: The OpenAI client is initialized with the base URL and API key.
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print("Programa veikia. Klausk apie 'vilnius.txt' lietuviškai (Ctrl+C nutraukti)\n")

while True:
    user_input = input("Klausimas:")

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Tu esi naudingas padėjėjas, atsakinėk lietuviškai."},
            {"role": "user", "content": f"Štai dokumento turinys:\n{context}\n\nKlausimas: {user_input}"},
        ],
        temperature=1.1,
        top_p=1.0,
        model=model
    )

    print("Atsakymas:", response.choices[0].message.content)