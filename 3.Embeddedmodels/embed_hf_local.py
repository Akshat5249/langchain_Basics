from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "New Delhi is a capital of India"
# result = embedding.embed_query(text)

docs=[
    "Delhi is the Capital of India",
    "Mumbai is the Financial Capital of India",
    "Bangalore is the IT Capital of India"
]
result = embedding.embed_documents(docs)

print(str(result))