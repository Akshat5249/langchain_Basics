from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#1 make template 
chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
chat_history=[]
#2 load chat.txt
with open('chat.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#3 create prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
print(prompt)
