import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env file
load_dotenv()

# Initialize ChatOpenAI using RoutesMe endpoint
llm = ChatOpenAI(
    model="GPT-5.6-Luna",
    api_key=os.getenv("API_KEY"),
    base_url="https://routesme.online/v1"
)

# Invoke the model
response = llm.invoke("What is the capital of France?")
print(response.content)
