from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os

load_dotenv()

llm = ChatOpenAI(
    model = "GPT-5.6-Luna",
    api_key = os.getenv("API_KEY"),
    base_url = "https://routesme.online/v1",
  
)


messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love programming."),
]

result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
