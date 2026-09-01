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
from langchain_community.document_loaders import TextLoader , WebBaseLoader


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)
url = "https://www.91mobiles.com/hub/vivo-t5x-iqoo-z11x-india-price-increased-rs-4000/"

prompt = PromptTemplate(
    template = "Answer the following question \n {question} from the following text - \n {text}  ",
    input_variables = ['question', 'text']
)




loader = WebBaseLoader(url)
documents = loader.load() # as documents store karega memory mein

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"question" : "What is the price of vivo t5x in India?", "text" : documents[0].page_content})


print(result)

# print(len(documents)) # print karega content of the document
# print(documents[0].page_content)