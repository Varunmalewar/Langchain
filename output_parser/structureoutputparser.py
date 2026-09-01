from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv
import os

from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(  # type: ignore[call-arg]
    repo_id = "deepseek-ai/DeepSeek-V4-Flash-0731",
    task = "text-generation",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]


)
model = ChatHuggingFace(
    llm = llm
)


schema = [
    ResponseSchema(name = 'fact_1',description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2',description = 'Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3',description = 'Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about the topic {topic} \n {format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)


chain = template | model | parser




result = chain.invoke({'topic': 'black hole'})

print(result)

