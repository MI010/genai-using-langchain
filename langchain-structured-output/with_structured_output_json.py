from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()
json_schema ={
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": { 
            "type": "array",
            "items": {    "type": "string" },
            "description": "write the key themes discussed in the review."
        },
        "summury": { 
            "type": "string",
            "description": "A brief summary of the review."
        }, 
        "sentiment": { 
            "type": "string",
            "enum": ["pos","neg"],
            "description": "The sentiment of the review, either 'positive', 'negative' or 'neutral'."
        },
        "pros": { 
            "type": "array",
            "items": {    "type": "string" },
            "description": "List the pros mentioned in the review.",
            "nullable": True
        },
        "cons": { 
            "type": "array",
            "items": {    "type": "string" },
            "description": "List the cons mentioned in the review.",
            "nullable": True
        },
    },
    "required": ["key_themes", "summury", "sentiment"]
}
    

# INPUT -> LLM -> SENTIMENT & SUMURY OUTPUT

structured_model = model.with_structured_output(json_schema)
# result = structured_model.invoke(""" The hardware is greate, but the software is terrible. There are too many pre intalled apps that I don't use and can't remove.
#              Also the UI looks outdated compared to other phones in the same price range. Hoping for softw
result = structured_model.invoke(""" I recently upgraded to samsung galaxy, its an absolute powerhouse. SNapdrago 8 and gen 3
                                  blah blah blah
                                 
                                 pros: powerful processor.
                                 cons:bulky and heavy.""") 
print(result)


