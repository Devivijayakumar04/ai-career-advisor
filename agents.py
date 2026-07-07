import os
from crewai import Agent, LLM

llm = LLM(
    model=os.getenv("OPENAI_MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

career_advisor = Agent(
    role="🎯 Expert Career Advisor",
    goal="Provide the best single career recommendation with roadmap.",
    backstory="You are a friendly, smart, and confident career mentor.",
    llm=llm,
    verbose=False   # ❌ removes logs
)
