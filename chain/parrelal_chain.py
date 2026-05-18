from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel



load_dotenv()

model1 = ChatOpenAI()
llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)
model2 = ChatHuggingFace(llm=llm)

model3 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt1 = PromptTemplate(
    template="Generate a short and simple notes from the following text \n {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate 3 short question and answers based on the following notes: \n {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document: notes -> \n {notes} and quiz -> \n {quiz}",
    input_variables=["notes", "quiz"]
)


parser = StrOutputParser()
parallel_chain = RunnableParallel(
    notes=prompt1 | model1 | parser,
    quiz=prompt2 | model2 | parser
)
chain = parallel_chain | prompt3 | model3 | parser
response = chain.invoke(input={"topic": "The history of Artificial Intelligence"})
print(response)
chain.get_graph().print_ascii()