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
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)


loader = PyPDFLoader("document_loader/Data Analyst in 90 days PDF.pdf")

docs = loader.load()




splitter = CharacterTextSplitter(
    chunk_size = 100,
    
    chunk_overlap = 0, # benefit of chunk overlap is that it will give you more context of the document. It will help the model to understand the document better.

    separator = ""
)
result = splitter.split_documents(docs)

print(result[0].page_content) # it is list of chunks of the document. It will print first chunk of the document. You can iterate over the result to get all chunks of the document.