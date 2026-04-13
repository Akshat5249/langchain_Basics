from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=32 )

docs=[
    "Delhi is the Capital of India",
    "Mumbai is the Financial Capital of India",
    "Bangalore is the IT Capital of India"
]

result = embed.embed_documents(docs)

print(str(result))