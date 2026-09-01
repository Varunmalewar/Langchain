from langchain_openai import ChatOpenAI

import os 
from dotenv import load_dotenv

load_dotenv()

chatllm = ChatOpenAI(
    model = "DeepSeek-V4-Flash-0731",
    api_key = os.getenv("API_KEY"),
    base_url="https://routesme.online/v1",
    temperature = 0.5,
    max_tokens = 100
)

result = chatllm.invoke("write 5 line poem on cricket")
print(result.content)