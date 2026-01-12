from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct",
                            task="text-generation")
model = ChatHuggingFace(llm=llm)

#1st prompt: detailed report
template1 = PromptTemplate(
    template = "Write a detailed report on the following topic: {topic}",
    input_variables = ["topic"]
)

#2nd prompt: concise summary
template2 = PromptTemplate(
    template = "Summarize the following report in a concise manner: {report}",
    input_variables = ["report"]
)

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic":"Dark TV shows"})
print("summary: ", result)