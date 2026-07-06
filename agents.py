from crewai import Agent
from langchain_openai import ChatOpenAI
import streamlit as st

def create_career_agent():

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct:free",
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        openai_api_base=st.secrets["OPENAI_BASE_URL"]
    )

    return Agent(
        role="Senior Career Counselor",

        goal="Provide 3 clear, personalized career recommendations",

        backstory=(
            "You are an experienced career counselor.\n"
            "Identify user level, analyze interest, and suggest practical careers.\n\n"

            "Rules:\n"
            "- Give ONLY 3 careers\n"
            "- Use numbered format (1, 2, 3)\n"
            "- Keep each career short (1-2 lines)\n"
            "- Avoid generic answers\n"
            "- No repetition\n"
            "- Be supportive and clear"
        ),

        llm=llm,  # 🔥 THIS IS THE KEY LINE

        verbose=False,
        allow_delegation=False
    )
