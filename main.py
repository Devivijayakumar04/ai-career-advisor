import streamlit as st
import requests

API_KEY = st.secrets["OPENROUTER_API_KEY"]

st.title("🎓 AI Career Advisor")

user_input = st.text_input("Enter your interest:")

if st.button("Get Advice"):
    if user_input:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/openrouter/free",
                "messages": [
                    {"role": "user", "content": f"Suggest 3 careers for someone interested in {user_input}"}
                ]
            }
        )

        result = response.json()

        if "choices" in result:
            st.write(result["choices"][0]["message"]["content"])
        else:
            st.write(result)
