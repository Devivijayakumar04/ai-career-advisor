import os
from dotenv import load_dotenv
from crewai import Agent, LLM

# ✅ Load environment variables
load_dotenv()

# ✅ Get values safely
MODEL = os.getenv("OPENAI_MODEL_NAME") or "openrouter/meta-llama/llama-3-8b-instruct"
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENAI_API_BASE") or "https://openrouter.ai/api/v1"

# ✅ Safety check (VERY IMPORTANT)
if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing. Check your .env file.")

# ✅ Create LLM
llm = LLM(
    model=MODEL,
    api_key=API_KEY,
    base_url=BASE_URL
)

# ✅ Create Agent
career_advisor = Agent(
    role="🎯 Expert Career Advisor",
    goal="Provide the best single career recommendation with roadmap.",
    backstory="You are a friendly, smart, and confident career mentor.",
    llm=llm,
    verbose=False
)
