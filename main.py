import os
import time
import streamlit as st
from dotenv import load_dotenv
from crew import run_crew

# PDF imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load env
load_dotenv()

# Page config
st.set_page_config(page_title="AI Career Advisor", page_icon="🚀")

st.title("🚀 AI Career Advisor")
st.write("Get your personalized career roadmap powered by AI 💡")

st.info("⚠️ Free usage is limited. Avoid clicking too fast to prevent errors.")

user_input = st.text_input("🎯 Enter your career goal:")

# ⏱️ Cooldown control (ANTI-SPAM)
if "last_run" not in st.session_state:
    st.session_state.last_run = 0


# FORMAT OUTPUT
def format_output(text):
    text = str(text)
    text = text.replace("**", "")

    text = text.replace("Title:", "\n\n### 🎯 Title:\n")
    text = text.replace("Explanation:", "\n\n### 📝 Explanation:\n")
    text = text.replace("Why it suits the user:", "\n\n### ✅ Why it suits you:\n")

    return text


# CREATE PDF
def create_pdf(content):
    file_path = "career_plan.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):
        if line.strip() != "":
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 10))

    doc.build(story)
    return file_path


# BUTTON
if st.button("Generate Roadmap ✨"):

    current_time = time.time()

    # ⛔ Prevent rapid clicking (5 sec cooldown)
    if current_time - st.session_state.last_run < 5:
        st.warning("⏳ Please wait a few seconds before trying again.")
        st.stop()

    st.session_state.last_run = current_time

    if user_input.strip() == "":
        st.warning("⚠️ Please enter something first!")

    else:
        try:
            with st.spinner("🤖 Thinking... Please wait..."):

                time.sleep(2)  # slight delay (safe)

                result = run_crew(user_input)

            formatted_result = format_output(result)

            st.success("✅ Here’s your career roadmap:")
            st.markdown(formatted_result)

            pdf_file = create_pdf(formatted_result)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="📄 Download as PDF",
                    data=f,
                    file_name="career_roadmap.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            error_msg = str(e).lower()

            if "rate limit" in error_msg or "quota" in error_msg:
                st.error("🚫 API limit reached. Please wait 1–2 minutes and try again.")
            elif "api key" in error_msg:
                st.error("🔑 API key issue. Check your .env file.")
            else:
                st.error(f"⚠️ Unexpected error: {str(e)}")
