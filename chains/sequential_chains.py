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

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a 5 line summary of the report: {report}",
    input_variables = ['report']
)

parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

result = chain.invoke({"topic": "cricket"})

print(result)