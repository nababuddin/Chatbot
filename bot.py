import openai
import time

openai.api_key = "YOUR OPEN AI API KEY" # replace with your own API key

def generate_response(prompt):
    # generate response using OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # return the generated text
    return response.choices[0].text.strip()

print("Welcome to the ChatBOT demo!")
time.sleep(1)
while True:
    # get user input
    user_input = input("You: ")
    # generate response
    response = generate_response(user_input + "\nChatGPT:")
    # print response
    print("Bot:",response)
