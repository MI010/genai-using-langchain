from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema


# this is removed in updated file
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct",
                            task="text-generation")
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = 'give me 3 facts about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'Mars planet'})
result = model.invoke(prompt)
res = parser.parse(result.content)
print("Parsed output: ", res)