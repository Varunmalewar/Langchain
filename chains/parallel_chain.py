from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import SecretStr
from langchain_core.runnables import RunnableParallel



load_dotenv()

llm1 = ChatOpenAI(
    model = "GPT-5.6-Luna",
    api_key = SecretStr(os.environ["API_KEY"]),
    base_url = "https://routesme.online/v1"
)
llm2 = ChatOpenAI(
    model = "DeepSeek-V4-Flash-0731",
    api_key = SecretStr(os.environ["API_KEY"]),
    base_url = "https://routesme.online/v1"
)

prompt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text \n {text}",
    input_variables = ['text']


)
prompt2 = PromptTemplate(
    template = "Generate 5 short question answers from the following text \n {text}",
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = "Merge the provided notes and quiz into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | llm1 | parser,
        'quiz' : prompt2 | llm2 | parser
    }
)
merge_chain = prompt3 | llm1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"text": "The solar system is a vast and complex system of celestial bodies that orbit around the Sun. It consists of eight planets, including Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics and features. The solar system also contains dwarf planets, moons, asteroids, comets, and other small objects. The Sun's gravitational pull keeps all these objects in their respective orbits. The study of the solar system helps us understand the origins and evolution of our own planet and the universe as a whole."})

# print(result)

print(chain.get_graph().print_ascii()) # how chain works and how data flows through it