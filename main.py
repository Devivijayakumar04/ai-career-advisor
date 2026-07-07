import os
import streamlit as st
from dotenv import load_dotenv
from crew import run_crew

# PDF imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="AI Career Advisor", page_icon="🚀")

# UI Header
st.title("🚀 AI Career Advisor")
st.write("Get your personalized career roadmap powered by AI 💡")

# User input
user_input = st.text_input("🎯 Enter your career goal:")


# 🔧 FUNCTION: CLEAN OUTPUT FORMAT
def format_output(text):
    text = str(text)

    # ❌ Remove unwanted markdown stars
    text = text.replace("**", "")

    # ✅ Fix formatting
    text = text.replace("Title:", "\n\n### 🎯 Title:\n")
    text = text.replace("Explanation:", "\n\n### 📝 Explanation:\n")
    text = text.replace("Why it suits the user:", "\n\n### ✅ Why it suits you:\n")

    return text


# 🔧 FUNCTION: CREATE PDF
def create_pdf(content):
    file_path = "career_plan.pdf"  # ✅ FIXED PATH

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):
        if line.strip() != "":
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 10))

    doc.build(story)

    return file_path


# 🚀 BUTTON ACTION
if st.button("Generate Roadmap ✨"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter something first!")
    else:
        with st.spinner("🤖 Thinking... Please wait..."):
            result = run_crew(user_input)

        # ✅ Format result
        formatted_result = format_output(result)

        st.success("✅ Here’s your career roadmap:")
        st.markdown(formatted_result)

        # ✅ Generate PDF
        pdf_file = create_pdf(formatted_result)

        # ✅ Download button
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download as PDF",
                data=f,
                file_name="career_roadmap.pdf",
                mime="application/pdf"
            )
