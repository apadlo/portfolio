from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Andrzej Padło"
PAGE_ICON = ":wave:"
NAME = "Andrzej Padło"
DESCRIPTION = """
Test Development Engineer with extensive experience in backend/API and mobile 
network protocol testing, test automation, and web application development. Skilled in Python, AWS, SQL, GraphQL, and 
modern test frameworks. Experienced in healthcare and telecom domains, with a strong record of collaboration and 
continuous learning.
"""
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/andrzejpadlo/",
}
PROJECTS = {
    "🏆 Playwright Python Framework - Web UI automation using Playwright for Python (pytest, POM, async support)": "https://github.com/apadlo/playwright-python",
    "🏆 Python Selenium Framework - Web UI automation framework using Selenium, pytest, and Page Object Model": "https://github.com/apadlo/PythonSeleniumFramework",
    "🏆 Python Backend Testing Framework - Automated API and backend testing framework (pytest, BDD, Allure)": "https://github.com/apadlo/PythonBackendTesting",
    "🏆 Python Appium Framework - Mobile app automation framework for Android/iOS using Appium, pytest, and Page Object Model": "https://github.com/apadlo/PythonAppiumFramework",
    "🏆 Pytest support for Django project backend tests - Simple ToDoWoo web app with user login and database-backed to-do lists": "https://github.com/apadlo/todos?tab=readme-ov-file#test-configuration",
    "🏆 ChatGPT-like Clone – Interactive web app simulating conversational AI, built with Streamlit and Python": "https://bielik.streamlit.app/",
    "🏆 AI-Powered Web Scraper – Streamlit app for automated web data extraction using Python and AI agent": "https://smart-scrapper.streamlit.app/",
    "🏆 Python AI Agent – Generates notes based on received prompt, built with FastAPI, LangChain, OpenAI": "https://github.com/apadlo/python-ai-agent",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    # Replace email with a contact button
    contact_button = st.button("📧 Contact Me")
    if contact_button:
        st.markdown(
            '<meta http-equiv="refresh" content="0; url=mailto:apadlo@hotmail.com">',
            unsafe_allow_html=True
        )
    st.link_button(
        "🔗 Visit my LinkedIn",
        SOCIAL_MEDIA["LinkedIn"]
    )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Over 15 years of experience in software testing and test automation, with a focus on backend/API and mobile network protocols
- ✔️ Strong hands-on experience in Python (pytest, BDD), SQL, AWS, GraphQL, MongoDB, Gitlab, Linux
- ✔️ Proven track record in designing, implementing, and maintaining automated test frameworks for backend APIs and mobile devices
- ✔️ Experience in healthcare and telecom industries, collaborating with cross-functional teams and reporting bugs
- ✔️ ISTQB Foundation certified, with continuous upskilling in Python, Django, and modern testing tools
    """
)



# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 🧑‍💻 Programming & Automation: Python (pytest, BDD, Selenium, Playwright), SQL, Django, Bash
- ☁️ Cloud & Tools: AWS, Gitlab, Linux, Jira, Bitbucket, Allure, Postman
- 🗄️ Databases: MongoDB, PostgreSQL, MySQL
- 🔗 APIs: REST, GraphQL, CLI testing
- 📱 Mobile & Protocols: Android Comms Test Suite, NAS, IMS (VoLTE, VoWiFi, RCS), 5G NR, 4G LTE, WCDMA, GSM
- 🏥 Domain: Healthcare IT, Pharma, Telecom
    """
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Sample Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Test Development Engineer | Sii Poland**")
st.write("03/2023 - Present")
st.write(
    """
- Built and maintained automated test frameworks using Python and pytest, applying OOP principles for scalability and reuse.
- Delivered comprehensive REST and GraphQL API testing using requests, Postman, and cURL.
- Implemented Allure Reports to provide clear, actionable test results and improve defect visibility.
- Created data-driven tests with Pandas to validate complex datasets and test outcomes.
- Automated UI regression tests using Playwright / Selenium / Splinter, following the Page Object Model (POM).
- Integrated automated tests into GitLab CI/CD pipelines, including secure secrets management.
- Supported cloud and containerized environments using AWS (RDS, S3, EKS), Docker, and basic Kubernetes concepts.
- Worked with PostgreSQL, GraphQL, MongoDB, Snowflake, and Linux environments, using Bash scripting to automate test and CI/CD tasks
    """
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior Protocol Test Engineer | Samsung Electronics Polska**")
st.write("03/2017 - 03/2023")
st.write(
    """
- Developed and maintained automated test cases for mobile network protocol tests on Android devices (Python, Git, Jira, Linux, Android Comms Test Suite)
- Backend development of CRUD web application for test management (Python, Django, Jira, Git, Bitbucket)
- Manual testing of Android mobile phones, tablets, and wearables
- NAS protocol testing in mobile and stationary NR/LTE/WCDMA/GSM environments
- Onsite IMS (VoLTE, VoWiFi, RCS) testing in 30+ European countries
- Frequent business travel (50% worktime)
    """
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Protocol Test Engineer | Samsung Electronics Polska**")
st.write("05/2010 - 03/2017")
st.write(
    """
- Conducted mobile software tests according to procedures
- Field, interoperability, and network operator acceptance tests
- Reported test results and registered problems
- Improved test procedures and processes
- Frequent business travel (50% worktime)
    """
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Test Team Lead | Samsung Electronics Polska**")
st.write("12/2007 - 05/2010")
st.write(
    """
- Managed a team of 15-20 testers
- Created test plans and reports
- Presented and shared results with management
- Cooperated with developers for quality assurance and bug fixing
    """
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Software Tester | Samsung Electronics Polska**")
st.write("08/2007 - 12/2007")
st.write(
    """
- Created and executed manual test cases (Test Forte, Anytest, MS Excel)
- Performed feature testing: SMS, MMS, Voice/Video call, Bluetooth, Wi-Fi
- Tested mobile phones based on Symbian, Windows Mobile, SHP
    """
)
