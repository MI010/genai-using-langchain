from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4", temperature=0, max_comppletion_tokens=10)
response = chat_model.invoke("write 5 lines of poem on nature.")
# print(response)
print(response.content)