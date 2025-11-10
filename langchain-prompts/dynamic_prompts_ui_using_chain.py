from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI()

st.header("🎬 Movie Assistant Tool")

user_input = st.selectbox("🎥 Select a movie", [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Godfather",
    "Pulp Fiction"
])

style_input = st.selectbox("Select explanation style", [
    "Concise",
    "Detailed",
    "Narrative",
    "Technical"
])

length_input = st.selectbox("Select explanation length", [
    "Short (1–2 paragraphs)",
    "Medium (3–4 paragraphs)",
    "Long (5–6 paragraphs)"
])

template = load_prompt("movie_summary_prompt_template.json")

if st.button("🎞️ Summarize"):

    chain = template | model
    result = chain.invoke({
    "user_input": user_input,
    "style_input": style_input,
    "length_input": length_input
   })
    
    st.markdown("🧠 Viola:")
    st.write(result.content)