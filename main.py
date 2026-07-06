import os
import streamlit as st

# 🔥 VERY IMPORTANT: Set environment variables BEFORE importing crew
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]
os.environ["OPENAI_MODEL_NAME"] = st.secrets["OPENAI_MODEL_NAME"]

from crew import run_crew  # import AFTER setting env

# UI Config
st.set_page_config(page_title="AI Career Advisor", page_icon="🎓")

st.title("🎓 AI Career Recommendation System")
st.write("Get personalized career guidance based on your interests.")

# Input
user_input = st.text_input("Enter your interest (e.g., coding, biology, business):")

# Button
if st.button("🚀 Get Career Advice"):
    if user_input:
        with st.spinner("Analyzing your interest..."):
            result = run_crew(user_input)
            st.markdown(result)
    else:
        st.warning("⚠️ Please enter your interest.")
