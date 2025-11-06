from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

st.header("Research Assistant Chatbot")
user_input = st.text_input("Enter your query:") 

if st.button("Summerize"):
    result = model.invoke(user_input)
    st.write("Response:", result.content)

