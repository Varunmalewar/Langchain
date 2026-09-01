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
from langchain_text_splitters import CharacterTextSplitter , RecursiveCharacterTextSplitter


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0,
)

chunks = splitter.split_text("This is a sample text that will be split into chunks using the RecursiveCharacterTextSplitter. The chunk size is set to 100 characters, and there is no overlap between the chunks. This means that each chunk will contain a maximum of 100 characters, and the next chunk will start immediately after the previous one ends. This is useful for processing large texts in smaller, manageable pieces.")

print(len(chunks)) # it will print the number of chunks created from the text
print(chunks[0])

