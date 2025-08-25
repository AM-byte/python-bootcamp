import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY_2")  # Pull the API key from environment variables
)

# Call the Chat Completion endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Hello! How are you today?"}
    ]
)

# Extract and print the assistant's reply
reply = response.choices[0].message.content
print("ChatGPT says:", reply)