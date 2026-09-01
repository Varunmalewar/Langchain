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



load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",   
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Summarize the following text in 50 words \n {text}",
    input_variables = ['text']
)

summarize_chain = RunnableSequence(prompt2, llm, parser)
report_gen_chain = RunnableSequence(prompt1, llm, parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 10 , summarize_chain),
    RunnablePassthrough()

)

final_result = RunnableSequence(report_gen_chain, branch_chain).invoke({"topic": "India"})

print(final_result)