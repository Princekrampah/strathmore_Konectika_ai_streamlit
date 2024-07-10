import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components

import time
import os

from utils.file_display.pdf_display import displayPDF

# Setup app with page title, icon and layout
st.session_state.page_title = "Strathmore KonecTika"
st.session_state.page_icon = ":shark:"
st.session_state.layout = "centered"


st.session_state.professional_skills = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "R",
    "Machine Learning", "Deep Learning", "Data Analysis", "Data Visualization",
    "Data Engineering", "Data Science", "Data Analytics", "Data Mining",
    "Data Warehousing", "Data Modeling", "Data Quality", "Data Governance",
    "Data Integration", "Data Migration", "Data Transformation", "Data Profiling",
    "Data Cleansing", "Data Wrangling", "Data Exploration", "Data Interpretation",
    "Data Reporting", "Data Management", "Data Strategy", "Data Architecture",
    "Data Security", "Data Privacy", "Data Ethics", "Data Compliance",
    "Big Data Technologies", "Hadoop", "Spark", "NoSQL Databases",
    "Cloud Computing", "AWS", "Azure", "Google Cloud Platform",
    "DevOps", "CI/CD", "Docker", "Kubernetes",
    "Software Development", "Object-Oriented Programming", "Functional Programming",
    "Version Control", "Git", "GitHub", "Agile Methodologies",
    "Project Management", "Scrum", "Kanban", "Team Collaboration",
    "Problem Solving", "Critical Thinking", "Analytical Skills", "Communication Skills",
    "Leadership", "Teamwork", "Time Management", "Adaptability",
    "Technical Writing", "Public Speaking", "Presentation Skills",
    "Artificial Intelligence", "Natural Language Processing", "Computer Vision",
    "Robotics", "Internet of Things (IoT)", "Blockchain",
    "Cybersecurity", "Network Security", "Penetration Testing",
    "Mobile Development", "Android Development", "iOS Development",
    "Game Development", "Unity", "Unreal Engine",
    "Software Testing", "Unit Testing", "Integration Testing", "Test Automation",
    "APIs", "REST", "GraphQL",
    "UX/UI Design", "Human-Computer Interaction", "User Experience",
    "Customer Experience", "Design Thinking", "Prototyping",
    "Business Intelligence", "Tableau", "Power BI",
    "Marketing Analytics", "SEO", "Digital Marketing",
    "Financial Analysis", "Econometrics", "Statistical Analysis",
    "Research Methods", "Survey Design", "Experimental Design",
    "Content Creation", "Blogging", "Video Production",
    "Ethical Hacking", "White-Hat Hacking", "Incident Response",
    "Sustainability", "Green Technologies", "Environmental Impact",
    "Social Impact", "Nonprofit Management", "Policy Analysis"
]

# set page configs
st.set_page_config(
    page_title=st.session_state.page_title,
    page_icon=st.session_state.page_icon,
    layout=st.session_state.layout,
    initial_sidebar_state="expanded",
)

st.sidebar.success(
    "Welcome to Strathmore KonecTika, use the links above to navigate the app.")


st.markdown("#### User Personal Details")
with st.form('user_details'):
    username = st.text_input("Username", placeholder="Enter your username")
    email = st.text_input("Email", placeholder="Enter your email")
    nationality = st.text_input(
        "Nationality", placeholder="Enter your Nationality")
    linkedIn = st.text_input("LinkedIn", placeholder="Enter your LinkedIn URL")
    phone_numer = st.text_input(
        "Phone Number", placeholder="Enter your phone number")
    personal_motor = st.text_input(
        'Personal Motor', placeholder="Enter your personal motor")
    # select most relevant tools with respect to the job
    professional_skills = st.multiselect(
        'Professional Skills', st.session_state.professional_skills)
    personal_detail_submit_btn = st.form_submit_button(
        'Submit Personal Details')


st.markdown("#### User Profile Details Generation")
with st.form('user_profile'):
    # profile
    user_profile = st.text_area("Profile")

    profile_details_submit_btn = st.form_submit_button('Submit')


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### User Education Details #One")
    with st.form('user_education_one'):
        education_title = st.text_input(
            "Title", placeholder="Enter your education title")
        education_duration = st.text_input(
            "Education Duration", placeholder="Enter your education duration")
        education_description = st.text_area(
            "Description", placeholder="Enter your education description")

        user_education_one_submit_btn = st.form_submit_button(
            'Submit Edcuation One')


with col2:
    st.markdown("#### User Education Details #Two")
    with st.form('user_education_two'):
        education_title = st.text_input(
            "Title", placeholder="Enter your education title")
        education_duration = st.text_input(
            "Education Duration", placeholder="Enter your education duration")
        education_description = st.text_area(
            "Description", placeholder="Enter your education description")

        user_education_two_submit_btn = st.form_submit_button(
            'Submit Edcuation Two')


st.markdown("#### User Education Details #Three")
with st.form('user_education_three'):
    education_title = st.text_input(
        "Title", placeholder="Enter your education title")
    education_duration = st.text_input(
        "Education Duration", placeholder="Enter your education duration")
    education_description = st.text_area(
        "Description", placeholder="Enter your education description")

    user_education_three_submit_btn = st.form_submit_button(
        'Submit Edcuation Three')


st.markdown("#### Job ID")
with st.form('job_id'):
    # job id
    job_id = st.text_input("Job ID")
    job_id_submit_btn = st.form_submit_button('Submit Job ID')


generate_btn = st.button("Generate CV")

if generate_btn:
    st.warning("Generating CV, please wait...")
    time.sleep(30)
    st.success("CV generated successfully, you can download it!")

    file_path = "./generated_html/generated_pdf.pdf"
    absolute_path = os.path.abspath(file_path)
    

    with open(absolute_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download Generated CV",
                       data=PDFbyte,
                       file_name="test.pdf",
                       mime='application/octet-stream')

# rush testing, needs removing
# /mount/src/
file_path = "./generated_html/generated_pdf.pdf"
absolute_path = os.path.abspath(file_path)


# Create modal
modal = Modal(
    "Generated CV",
    key="generated_cv",
    # Optional
    padding=20,
    max_width=1000
)

view_pdf = st.button("View Generated CV", disabled= (not generate_btn))

if view_pdf:
    modal.open()

if modal.is_open():
    with modal.container():
        displayPDF(absolute_path, st)
