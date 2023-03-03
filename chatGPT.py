import os
import openai
openai.api_key = "API_KEY_HERE"

messages=[]
print("Welcome to ChatGPT using the OpenAI API")
print("")

while True:
    prompt = input("User Prompt: ")
    if prompt == 'exit':
        break

    messagesUser= {"role": "user", "content": prompt}
    messages.append(messagesUser)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1024,
        temperature=0
    )

    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    
    print()
    print("USER: " + prompt)
    print(response.choices[0].message.content)
