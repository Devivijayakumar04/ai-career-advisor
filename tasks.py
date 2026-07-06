from crewai import Task

def create_career_task(agent, user_interest):
    return Task(
        description=f"""
Student Interest: "{user_interest}"

Generate a SHORT, structured, and practical response.

🎯 Top 3 Career Recommendations:

1. Career Name
   - Skills: (3 skills only)
   - Tools: (2 tools only)
   - Learn From:
     • 1 course
     • 1 free resource
   - Next Steps:
     1. Step 1
     2. Step 2

2. Career Name
   - Skills: (3 skills only)
   - Tools: (2 tools only)
   - Learn From:
     • 1 course
     • 1 free resource
   - Next Steps:
     1. Step 1
     2. Step 2

3. Career Name
   - Skills: (3 skills only)
   - Tools: (2 tools only)
   - Learn From:
     • 1 course
     • 1 free resource
   - Next Steps:
     1. Step 1
     2. Step 2

IMPORTANT:
- Max 180 words TOTAL
- No explanations
- No repetition
- Keep it clean, simple, and useful
""",
        agent=agent,
        expected_output="3 structured career paths with skills, tools, learning, and action steps"
    )