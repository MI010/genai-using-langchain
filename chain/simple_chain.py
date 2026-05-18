from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate a slogan for the company {company}",
    input_variables=["company"]
)

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()
chain = prompt | model | parser   
response = chain.invoke(input={"company": "Apple"})
print(response)

chain.get_graph().print_ascii()