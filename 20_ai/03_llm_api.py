
key = "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"

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