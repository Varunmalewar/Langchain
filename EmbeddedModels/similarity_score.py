from langchain_huggingface import HuggingFaceEndpointEmbeddings
import os 
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model = "Qwen/Qwen3-Embedding-4B",
    huggingfacehub_api_token = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"],

)
documents = [
    "Mumbai is the financial capital of India.",
    "The Gateway of India is a famous monument in Mumbai.",
    "Bollywood is the heart of the Indian film industry.",
    "Mumbai has a rich cultural heritage and diverse cuisine.",
    "The city is known for its bustling markets and vibrant street life."]

query = "What is Mumbai known for?"
query_embedding = embedding.embed_query(query)
document_embeddings = embedding.embed_documents(documents)

scores = cosine_similarity([query_embedding], document_embeddings)[0]

index , score = sorted(enumerate(scores),key = lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Smilarity Score: ", score)



