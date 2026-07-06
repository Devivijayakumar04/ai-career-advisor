import streamlit as st
from crew import run_crew

st.set_page_config(page_title="AI Career Advisor", page_icon="🎓")

st.title("🎓 AI Career Recommendation System")
st.write("Get personalized career guidance based on your interests.")

user_input = st.text_input("Enter your interest (e.g., coding, biology, business):")

if st.button("🚀 Get Career Advice"):
    if user_input:
        with st.spinner("Analyzing your interest..."):
            result = run_crew(user_input)
            st.markdown(result)
    else:
        st.warning("⚠️ Please enter your interest.")