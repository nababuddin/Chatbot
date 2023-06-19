import openai
import time

def generate_response(prompt):
    # Generate response using OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Return the generated text
    return response.choices[0].text.strip()

print("Welcome to the ChatBOT demo!")
time.sleep(1)

# Get user's OpenAI API key
api_key = input("Please enter your OpenAI API key: ")
openai.api_key = api_key

while True:
    # Get user input
    user_input = input("You: ")
    # Generate response
    response = generate_response(user_input + "\nChatGPT:")
    # Print response
    print("Bot:", response)
