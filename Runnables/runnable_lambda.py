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

def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ['topic']
)

joke_gen_chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel(
{    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
    }
)

final_chain  = RunnableSequence(joke_gen_chain, parallel_chain)

final_result = final_chain.invoke({"topic": "cricket"})

ulti_final_result = """ {} \n word count : {}""".format(final_result['joke'],final_result['word_count'])
print(ulti_final_result)

