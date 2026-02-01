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
Test Development Engineer and Senior Protocol Test Engineer with extensive experience in backend/API and mobile 
network protocol testing, automation, and web application development. Skilled in Python, AWS, SQL, GraphQL, and 
modern test frameworks. Experienced in healthcare and telecom domains, with a strong record of collaboration and 
continuous learning.
"""
# EMAIL = "johndoe@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
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


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


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
st.subheader("Hard Skills")
st.write(
    """
- 🧑‍💻 Programming & Automation: Python (pytest, BDD, Selenium), SQL, Django, Bash
- ☁️ Cloud & Tools: AWS, Gitlab, Linux, Jira, Bitbucket, Allure, Postman
- 🗄️ Databases: MongoDB, PostgreSQL, MySQL
- 🔗 APIs: REST, GraphQL, CLI testing
- 📱 Mobile & Protocols: Android Comms Test Suite, NAS, IMS (VoLTE, VoWiFi, RCS), 5G NR, 4G LTE, WCDMA, GSM
- 🏥 Domain: Healthcare IT, Pharma, Telecom
    """
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Test Development Engineer | Sii Poland**")
st.write("03/2023 - Present")
st.write(
    """
- Testing an advanced AWS-based platform for a healthcare industry client (demand for medicines, clinical trial process, etc.)
- Tool stack: AWS, SQL, GraphQL, MongoDB, Gitlab, Linux
- Create and maintain automated backend API and CLI tests in Python using BDD (pytest, allure)
- Report bugs and collaborate with the development team on resolving them
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
- Frequent business trips (London, Frankfurt, Paris, Moscow, Milan, Stockholm)
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
