from crewai import Agent

def create_career_agent():
    return Agent(
        role="Career Advisor",
        goal="Suggest careers based on user interest",
        backstory="Expert in career guidance",
        verbose=True
    )
