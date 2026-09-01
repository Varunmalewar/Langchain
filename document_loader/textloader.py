from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import SecretStr
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from  typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda,RunnableSequence, RunnablePassthrough
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)

prompt = PromptTemplate(
    template = "Write a summary for the following {topic}  ",
    input_variables = ['topic']
)
parser = StrOutputParser()

chain = prompt | llm | parser




loader = TextLoader("document_loader/sample.txt", encoding="utf-8")
documents = loader.load() # as documents store karega memory mein

print("Meta data of the file is :\\n",documents[0].metadata)
print("")



print(chain.invoke({"topic" : documents[0].page_content})) # print karega summary of the document
