import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.responses.create(
    model="gpt-5",
    instructions="You are a coding assistant that talks like a pirate.",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)

for choice in response.choices:
    print(choice.input)