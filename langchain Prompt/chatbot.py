from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="GLM5.3-flash",
    api_key=os.getenv("API_KEY"),
    base_url="https://routesme.online/v1",
)

chat_history = [
    SystemMessage(content = "You  are a helpful assistant" )
]

# loop infinitely run karega jab tak user manually stop na kare
while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: " , result.content)

print("Chatbot session ended with chat history as ", chat_history, ".")
