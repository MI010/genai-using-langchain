from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
query = "What is the capital of Germany?"
embedding = embedding_model.embed_query(query)
print(str(embedding))