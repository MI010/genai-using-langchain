from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI()

st.header("Research Assistant Tool")
user_input = st.text_input("Enter your query:") 

if st.button("Summerize"):
    result = model.invoke(user_input)
    st.write("Response:", result.content)



    