from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({"topic":"Dark TV shows"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"report":result.content})
summary = model.invoke(prompt2)

print("summary: ", summary.content)
