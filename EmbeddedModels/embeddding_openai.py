from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()

embedding = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    api_key = SecretStr(os.environ["API_KEY"]),
    # base_url = "https://routesme.online/v1",
    dimensions = 32,

)

result = embedding.embed_query("Mumbai Meri Jaan!")
print(str(result) + "\n")
print(len(result))