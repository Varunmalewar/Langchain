from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import SecretStr


load_dotenv()

llm = ChatOpenAI(
    model = "GPT-5.6-Luna",
    api_key = SecretStr(os.environ["API_KEY"]),
    base_url = "https://routesme.online/v1"
)

parser = StrOutputParser()


prompt = PromptTemplate(
    template = "Generate 5 intresting facts about {topic}",
    input_variables = ['topic']
)

chain = prompt | llm | parser
result = chain.invoke({"topic": "cricket"})
print(result)



