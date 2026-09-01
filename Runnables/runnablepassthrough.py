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
    template = "Write a joke about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke {text}",
    input_variables = ['text']
)

joke_parsing = RunnableSequence(prompt1, llm, parser)

   


parallel_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough(),
        'explanation' : RunnableSequence(joke_parsing, prompt2, llm, parser)


    }
)
final_chain = RunnableSequence(joke_parsing, parallel_chain)

result = final_chain.invoke({"topic": "cricket"})
print(result)
