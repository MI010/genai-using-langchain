from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct",
                            task="text-generation")
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()
template = PromptTemplate(
    template = 'give me name, age, and city of a fictional person \n {format_instruction}',
    input_variables = [],
    partial_variables={"format_instruction": parser.get_format_instructions()}
    
)

template = PromptTemplate(
    template = 'give me 5 facts about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
    
)

# prompt = template.format()

# result = model.invoke(prompt)
# res = parser.parse(result.content)
chain = template | model | parser
result = chain.invoke({'topic':'Mars planet'})
print("Parsed output: ", result)