from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

template = ChatPromptTemplate([
    ('system','You are a helpful {domain} assistant.'),
    ('human','Explain in simple terms: {topic}')
])

prompt = template.invoke({
    "domain": "movie",
    "topic": "Inception"
})

print(prompt)