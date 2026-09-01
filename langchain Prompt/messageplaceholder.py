from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import HumanMessage


# chat template 
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent"),
     MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')

])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history = f.readlines()

# create prompt
prompt = chat_template = chat_template.invoke({
    'chat_history': chat_history,
    'query': "I have an issue with my order. Can you help me?"
})

print(prompt.to_string())