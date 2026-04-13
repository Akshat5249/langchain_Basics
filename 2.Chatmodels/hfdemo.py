from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="gpt2",
    provider="hf-inference",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    temperature=0,
    max_new_tokens=100
)

result = llm.invoke("What is the capital of India?")

print(result.strip())
