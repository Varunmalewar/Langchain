from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(  # type: ignore[call-arg]
    repo_id = "zai-org/GLM-5.3",
    task = "conversational",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]


)
model = ChatHuggingFace(
    llm = llm
)

template = PromptTemplate(
    template = "Give me the name , age , city of a fictional person \n {format_instructions} \n",
    input_variables = [],
    partial_variables = {
        "format_instructions": JsonOutputParser().get_format_instructions()
    }
)

prompt = template.format()

# result = model.invoke(prompt)

# parser = JsonOutputParser()
# result = parser.parse(result.content)
# print(result)
# print(type(result))
# print(result['name'])

chain =  template | model | JsonOutputParser()

result = chain.invoke({})
print(result)
print(type(result))
print(result['name'])
