from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    # model="anthropic/claude-3-haiku", 
    model = "openai/gpt-3.5-turbo",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

chat_history = [
    SystemMessage(content='you are a helpful Ai assistant')
]

while True :
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit' :
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI: ",result.content)

print(chat_history)
print("Thank You")
