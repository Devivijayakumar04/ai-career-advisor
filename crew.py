from crewai import Crew
from tasks import create_task
from agents import career_advisor

def run_crew(user_input):

    task = create_task(user_input)   # ✅ using your tasks.py

    crew = Crew(
        agents=[career_advisor],
        tasks=[task],
        verbose=False   # ❌ no logs
    )

    result = crew.kickoff()
    return result
