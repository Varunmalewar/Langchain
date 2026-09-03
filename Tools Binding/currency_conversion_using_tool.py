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
# from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.tools import tool
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)

@tool
def get_conversion_factor(base_currency : str, target_currency : str)->float :
    """What is the conversion factor from base_currency to target_currency using an API"""
    url = f"https://v6.exchangerate-api.com/v6/572afd7ca7b8177f4c76f6b9/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rate"]

@tool
def convert_currency(base_currency_value : float, conversion_rate : Annotated[float,InjectedToolArg])->float :
    """Convert base_currency_value to target currency using the conversion factor"""
    return base_currency_value * conversion_rate


llm_with_tools = llm.bind_tools([get_conversion_factor, convert_currency])

messages = [HumanMessage(content="What is the conversion factor between USD and INR? and then convert 10 USD to INR using the conversion factor")]

result = llm_with_tools.invoke(messages)
messages.append(result)


# Round 1: run the tool the model asked for → get the conversion factor
factor = get_conversion_factor.invoke(result.tool_calls[0])
messages.append(factor)


# Round 2: model now asks to convert — WITHOUT conversion_rate (it's InjectedToolArg)
result = llm_with_tools.invoke(messages)
messages.append(result)


# We inject the rate ourselves — the LLM never provides it
result.tool_calls[0]["args"]["conversion_rate"] = float(factor.content)
converted = convert_currency.invoke(result.tool_calls[0])
messages.append(converted)


# Round 3: final answer
print(llm_with_tools.invoke(messages).text)

