from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

msg = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about langchain')
]

result = model.invoke(msg) 

msg.append(AIMessage(content=result.content))

print(msg)
# print("\n--- Conversation ---\n")
# for m in msg:
#     if isinstance(m, SystemMessage):
#         print(f"System: {m.content}\n")
#     elif isinstance(m, HumanMessage):
#         print(f"Human: {m.content}\n")
#     elif isinstance(m, AIMessage):
#         print(f"AI: {m.content}\n")