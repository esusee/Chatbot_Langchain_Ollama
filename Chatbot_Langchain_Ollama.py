from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st

st.title("Susee's Chat Bot")
input_txt = st.text_input("search your questions")

prompt = ChatPromptTemplate.from_messages(
    [("system","You are the AI assiatant. Your name is lama"),
     ("user","You asked:{query}")
        ])

lama=ollama(model="llama2")
output = StrOutputParser()
chain = prompt|lama|output

if input_txt:
    st.write(chain.invoke({"query":input_txt}))