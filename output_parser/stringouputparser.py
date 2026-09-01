from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(  # type: ignore[call-arg]
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
    task = "text-generation",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]


)
model = ChatHuggingFace(
    llm = llm
)
# 1st point prompt ->detailed report
template1 = PromptTemplate(  # type: ignore[call-arg]
    input_variables = ['topic'],
    template = "write a detailed report on the topic: {topic}"
)


# 2nd prompt -> summary
template2 = PromptTemplate(  # type: ignore[call-arg]
    input_variables = ['text'],
    template = "write a 5 line summary of the topic: {text}"
)

chain =  template1 | model | StrOutputParser() | template2 | model | StrOutputParser()

result = chain.invoke({"topic": "black hole"})

print(result)



