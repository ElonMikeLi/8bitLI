# this is a project about langchain !

# print('hellow world')

import os
from openai import OpenAI

client = OpenAI(
	api_key= os.environ.get('API_key'),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
	model='deepseek-chat',
    messages=[
    	{"role": "system", "content":"你是我的私人助理！"}，
    	{"role": "user", "content": "你好，你是干嘛的！"}
    ],
    stream = false
)

print(response.choices[0].message.content)