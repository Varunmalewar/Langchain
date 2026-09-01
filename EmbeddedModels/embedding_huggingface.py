from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"],
    
)

result = embedding.embed_query("Mumbai Meri Jaan!")
print(str(result) + "\n")
print(len(result))
