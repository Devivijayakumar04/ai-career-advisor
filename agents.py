from crewai import Agent

def create_career_agent():
    return Agent(
        role="Senior Career Counselor",
        goal="Provide 3 clear, personalized career recommendations",
        backstory="You are an expert career advisor helping students.",
        verbose=True,
        allow_delegation=False
    )
