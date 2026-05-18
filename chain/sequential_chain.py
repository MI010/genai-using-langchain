from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following report in 2 lines: \n {report}",
    input_variables=["report"]
)

model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke(input={"topic": "Climate Change"})
print(response)
chain.get_graph().print_ascii()
