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


# 🔥 NEW IMPROVED PDF FUNCTION
def create_pdf(content):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER

    file_path = "career_plan.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        name="HeadingStyle",
        parent=styles["Heading2"],
        spaceAfter=10
    )

    normal_style = styles["Normal"]

    story = []

    # ❌ Remove emojis (prevents ■ issue)
    content = content.replace("🎯", "")
    content = content.replace("📝", "")
    content = content.replace("✅", "")
    content = content.replace("🚀", "")
    content = content.replace("💡", "")

    lines = content.split("\n")

    for line in lines:
        line = line.strip()

        if not line:
            story.append(Spacer(1, 10))
            continue

        # Title
        if "Career Recommendation" in line:
            story.append(Paragraph("Career Recommendation", title_style))

        # Headings
        elif "Title:" in line:
            story.append(Paragraph("Title", heading_style))

        elif "Explanation:" in line:
            story.append(Paragraph("Explanation", heading_style))

        elif "Why it suits you:" in line:
            story.append(Paragraph("Why it suits you", heading_style))

        # Bullet points
        elif line.startswith("-"):
            story.append(Paragraph(f"• {line[1:].strip()}", normal_style))

        # Normal text
        else:
            story.append(Paragraph(line, normal_style))

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

                time.sleep(2)

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
