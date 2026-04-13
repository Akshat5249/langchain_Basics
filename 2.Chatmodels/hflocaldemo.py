from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs=dict(
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)
#result=model.invoke("What is capital of india")
#result=model.invoke("Who is CM of Tamil nadu")

result=model.invoke("write a paragraph about Gandhiji")
result=model.invoke("total number of mountain peaks in nepal")

print(result.content)
