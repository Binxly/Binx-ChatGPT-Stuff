import os
import openai
openai.api_key = "YOUR_API_KEY"

messages=[]
print("Welcome to ChatGPT using the OpenAI API")

while True:
    prompt = input("\nUser: ")
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
    
    print("\n" + response.choices[0].message.content)
