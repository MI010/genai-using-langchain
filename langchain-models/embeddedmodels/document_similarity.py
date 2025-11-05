from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
documents = [
    "Masum works at Sapient.",
    "Deepa works at Accenture",
    "Mugdha works at MSCI",
    "Piyush works at xy5",
    "Aditya works at JP Morgan",
    "Sarvesh works at Capgimini"
]   
query = "Tell me about employees working at Accenture and Sapient."
query1 = "Tell me about employees working at Accenture"

doc_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)
query1_embedding = embedding_model.embed_query(query1)

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
similarities1 = cosine_similarity([query1_embedding], doc_embeddings)[0]

print("Similarities for query 1:", similarities)
print("Similarities for query 2:", similarities1)

print(sorted(list(enumerate(similarities)),key= lambda x:x[1],reverse=True))
print(sorted(list(enumerate(similarities1)),key= lambda x:x[1],reverse=True))

index, score = sorted(list(enumerate(similarities)),key= lambda x:x[1])[-1]
index1, score11 = sorted(list(enumerate(similarities1)),key= lambda x:x[1])[-1]
print(query)
print(f"Most similar document (score: {score}): {documents[index]}")
print(query1)
print(f"Most similar document (score: {score11}): {documents[index1]}")