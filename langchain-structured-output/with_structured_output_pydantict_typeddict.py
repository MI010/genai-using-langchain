from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()
class Review(BaseModel):
    key_themes: list[str] = Field(..., description="write the key themes discussed in the review.")
    summury : str = Field(..., description="A brief summary of the review.")
    sentiment : Literal["pos","neg"] = Field(..., description="The sentiment of the review, either 'positive', 'negative' or 'neutral'.")
    pros : Optional[list[str]] = Field(None, description="List the pros mentioned in the review.")
    cons : Optional[list[str]] = Field(None, description="List the cons mentioned in the review.")
    name : Optional[str] = Field(None, description="The name of the reveiwer.")  
    

# INPUT -> LLM -> SENTIMENT & SUMURY OUTPUT

structured_model = model.with_structured_output(Review)
# result = structured_model.invoke(""" The hardware is greate, but the software is terrible. There are too many pre intalled apps that I don't use and can't remove.
#              Also the UI looks outdated compared to other phones in the same price range. Hoping for softw
result = structured_model.invoke(""" I recently upgraded to samsung galaxy, its an absolute powerhouse. SNapdrago 8 and gen 3
                                  blah blah blah
                                 
                                 pros: powerful processor.
                                 cons:bulky and heavy.""") 
print(result)


