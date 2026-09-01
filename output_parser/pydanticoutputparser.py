from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(  # type: ignore[call-arg]
    repo_id = "zai-org/GLM-5.3-Flash",
    task = "text-generation",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]
)
model = ChatHuggingFace(
    llm = llm
)

class Person(BaseModel):
    name : str = Field(..., description="The name of the person")
    age : int = Field(gt = 18 , description="The age of the person (must be greater than 18)")
    city : str = Field(description = "The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Generate the name , age and city of fictional {place} person \n {format_instructions}",
   
    input_variables = ['place'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}

)

# prompt = template.invoke({"place": "Indian"})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser

result = chain.invoke({"place": "Indian"})
print(result)