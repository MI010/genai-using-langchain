from langchain_huggingface import HuggingFaceEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text = "The capital of Italy is Rome."
embedding = embedding_model.embed_query(text)

print("Embedding length:", len(embedding))
print("First 8 values:", embedding[:8])

documents = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
]
embedding11 = embedding_model.embed_documents(documents)
# print("Number of document embeddings:", len(embedding))
# print("Length of first document embedding:", len(embedding[0]))
print(str(embedding11))