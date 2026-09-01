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
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    api_key = SecretStr(os.environ["GOOGLE_API_KEY"]),

)

loader = DirectoryLoader(
    path = "document_loader",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

docs  = loader.lazy_load() # as documents store karega memory mein
# print(len(docs))
# print(docs[2].page_content) # print karega content of the document
# print("Meta data of the file is :\\n",docs[2].metadata)

for doc in docs:
    # print(doc.page_content)
    print("Meta data of the file is :\\n",doc.metadata)
