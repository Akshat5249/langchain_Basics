#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# llm = OpenAI(model = 'gpt-3.5-turbo-instruct')
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",  
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=1,
    max_completion_tokens=10
)

# result = llm.invoke("write a 5 line poem on cricket")
result = llm.invoke("what is the capital of india")
# print(result)
print(result.content)