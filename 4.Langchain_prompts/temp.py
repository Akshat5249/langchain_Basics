from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4",  
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=1,# same temp pr same output rehta hai 
    max_completion_tokens=100
)

result = llm.invoke("Write a 5 line poem on cricket")

print(result.content)