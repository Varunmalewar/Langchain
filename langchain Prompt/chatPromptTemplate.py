from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Please explain in simple terms what is {topic}")
])


prompt = chat_template.invoke({
    'domain' : "Cricket",
    'topic' : "Duckworth-Lewis method"
})

print(prompt.to_string())