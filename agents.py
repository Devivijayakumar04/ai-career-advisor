from crewai import Agent
from crewai.llms import LiteLLM

def create_career_agent():
    
    llm = LiteLLM(
        model="openrouter/openrouter/free",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        api_base="https://openrouter.ai/api/v1"
    )

    return Agent(
        role="Senior Career Counselor",
        goal="Provide 3 clear, personalized career recommendations",
        backstory="You are an expert career advisor.",
        llm=llm,   # ✅ IMPORTANT
        verbose=False,
        allow_delegation=False
    )
