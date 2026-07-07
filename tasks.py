from crewai import Task
from agents import career_advisor

def create_task(user_input):
    task = Task(
        description=f"""
USER INPUT:
"{user_input}"

You are an EXPERT CAREER ADVISOR.

STRICT RULES:
- Give ONLY ONE best career
- No multiple suggestions
- Be confident and precise

OUTPUT FORMAT:

🎯 Career Recommendation
Title:
Explanation:
Why it suits the user:

🧠 Skills Required
Technical Skills:
- 

Soft Skills:
- 

🛠 Tools & Technologies:
- 

🚀 Learning Roadmap
Beginner:
- 

Intermediate:
- 

Advanced:
- 

📚 Courses & Resources
Free Courses:
- 

Paid Courses:
- 

Platforms:
- 

Certifications:
- 

💡 Projects to Build
Beginner:
- 

Intermediate:
- 

Advanced:

📈 Career Growth
Entry roles:
- 

Mid-level:
- 

Advanced roles:
- 

🛠 Action Plan
1.
2.
3.
4.
5.
""",

        expected_output="""
A structured career plan including:
- One career recommendation
- Explanation and reasoning
- Skills (technical + soft)
- Tools & technologies
- Learning roadmap
- Courses (free & paid)
- Certifications
- Projects
- Career growth
- Step-by-step action plan
""",

        agent=career_advisor
    )

    return task
