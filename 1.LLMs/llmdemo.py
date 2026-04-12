#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# llm = OpenAI(model = 'gpt-3.5-turbo-instruct')
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",  # OpenRouter format
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

result = llm.invoke("what is the capital of india")

print(result.content)