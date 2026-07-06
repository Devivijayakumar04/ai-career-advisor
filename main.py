import os
import streamlit as st

# ✅ SET ENV BEFORE ANY IMPORTS
os.environ["OPENAI_API_KEY"] = st.secrets["OPENROUTER_API_KEY"]
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

from crew import run_crew

st.title("🎓 AI Career Advisor")

user_input = st.text_input("Enter your interest:")

if st.button("Get Advice"):
    if user_input:
        result = run_crew(user_input)
        st.write(result)
