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
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda,RunnableSequence
import time


load_dotenv()

llm = ChatOpenAI(
    model = "z-ai/glm-5.3-free",
    api_key = SecretStr(os.environ["TK_API_KEY"]),
    base_url = "https://api.tokenrouter.com/v1"
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ['topic']

)

prompt2 = PromptTemplate(
    template = "Explain the following joke {text}",
    input_variables = ['text']

)
chain = RunnableSequence(prompt1 , llm , parser , prompt2 , llm , parser)

print(chain.invoke({"topic": "cricket"}))
   