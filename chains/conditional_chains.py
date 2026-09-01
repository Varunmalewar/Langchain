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
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
import time


load_dotenv()

llm = ChatOpenAI(
    model = "z-ai/glm-5.3-free",
    api_key = SecretStr(os.environ["TK_API_KEY"]),
    base_url = "https://api.tokenrouter.com/v1"
)

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment : Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback, either 'positive' or 'negative'.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1  =PromptTemplate(
    template = "Classify the sentiment of following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}

)

classifier_chain = prompt1 | llm | parser2

prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback: {feedback}",
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback: {feedback}",
    input_variables = ['feedback']
)


branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive',prompt2 | llm | parser),
    (lambda x : x.sentiment == 'negative',prompt3 | llm | parser),
    RunnableLambda(lambda x : "could not find sentiment in the feedback")
)

print(time.time())
chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "The product is really terrified and I am not satisfied with the quality."})

print(result)  # This will print the response generated based on the sentiment of the feedback
print(time.time())


result = classifier_chain.invoke({"feedback": "The product is really good and I am satisfied with the quality."})

print(result.sentiment)
graph = chain.get_graph()
print(graph.print_ascii())