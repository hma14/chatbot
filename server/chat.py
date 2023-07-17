import openai
import os
import sys

openai.api_key = os.environ['OPENAI_API_KEY']

messages = [{
    "role":
    "system",
    "content":"I want to create my own chat bot UI by calling chatGPT api with python, can you advise me how to start?" 
  }]
  

def start_chat(content):
  
  
  messages.append({"role": "user", "content": content})
  
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)
  
  chat_response = completion.choices[0].message.content
  #print(f'ChatGPT: {chat_response}')
  messages.append({"role": "assistant", "content": chat_response})
  
  return f'ChatGPT: {chat_response}'
  