from crewai import Crew
from agents import create_career_agent
from tasks import create_career_task

def run_crew(user_input):
    agent = create_career_agent()
    task = create_career_task(agent, user_input)

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process="sequential",   # ✅ ensures proper execution
        verbose=False
    )

    result = crew.kickoff()

    return str(result)   # ✅ ensures clean output for Streamlit