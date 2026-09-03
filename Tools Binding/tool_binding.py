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



load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)


@tool
def multiply(a: int, b:int) ->int :
    """Multiply a and b """
    return a * b

# print(multiply.invoke({"a": 5, "b": 3}))


llm_with_tools = llm.bind_tools([multiply])



query = HumanMessage(content="can you multiply 5 with 3?")

messages = [query]

result = llm_with_tools.invoke(messages)
messages.append(result)


tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

# print(messages)


print(llm_with_tools.invoke(messages).text)
