from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="google/gemma-4-26b-a4b-it:free",  
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# result = llm.invoke("Explain AI in simple terms")
result = llm.invoke("what is the capital of india")
print(result.content)