from crewai import Crew, Task
from agents import create_career_agent

def run_crew(user_input):

    agent = create_career_agent()

    task = Task(
        description=f"Suggest 3 careers for someone interested in {user_input}",
        agent=agent,
        expected_output="List of 3 careers with explanation"
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        llm={
            "model": "openrouter/openrouter/free"
        }  # ✅ THIS LINE FIXES EVERYTHING
    )

    result = crew.kickoff()
    return result
