from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()
class Review(TypedDict):
    sentiment: str
    sumurry: str

# INPUT -> LLM -> SENTIMENT & SUMURY OUTPUT

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(""" The hardware is greate, but the software is terrible. There are too many pre intalled apps that I don't use and can't remove.
             Also the UI looks outdated compared to other phones in the same price range. Hoping for software updates to improve the experience.""") 
print(result)
print("Sentiment: ", result['sentiment'])
print("Summary: ", result['sumurry'])  


