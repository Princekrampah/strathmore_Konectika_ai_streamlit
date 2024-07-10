import streamlit as st

# Setup app with page title, icon and layout
st.session_state.page_title = "Strathmore KonecTika"
st.session_state.page_icon = ":shark:"
st.session_state.layout = "centered"

# set page configs
st.set_page_config(
    page_title=st.session_state.page_title,
    page_icon=st.session_state.page_icon,
    layout=st.session_state.layout,
    initial_sidebar_state="expanded",
)

st.sidebar.success(
    "Welcome to Strathmore KonecTika, use the links above to navigate the app.")


st.title("About Us")

st.markdown("""
# About Us

Welcome to [Your Website Name]!

## Our Mission

At [Your Website Name], our mission is to provide high-quality content that educates, inspires, and empowers our audience. Whether it's through our blog posts, YouTube videos, or interactive quizzes, we aim to deliver valuable information and insights that help you grow and succeed.

## Who We Are

[Your Website Name] was founded by [Your Name], a passionate backend Python developer and AI enthusiast. With a background in web development and a love for sharing knowledge, [Your Name] created this platform to connect with like-minded individuals and create a community of learners and innovators.

## What We Do

### Blog
Our blog features a wide range of topics, including:
- Advanced AI systems and Agentic RAG systems
- Python development tips and tutorials
- Web development best practices
- Insights and experiences from our field studies

### YouTube Channel
On our YouTube channel, you'll find:
- In-depth tutorials and how-to videos
- Quizzes to test your knowledge and reinforce learning
- Insights into AI, web development, and more

### Projects
We are constantly working on exciting projects, such as:
- **Strathmore KonecTika**: A web application designed to help students get jobs by connecting them with opportunities and resources.

## Our Values

- **Education**: We believe in the power of education and strive to make learning accessible and enjoyable for everyone.
- **Innovation**: We are committed to exploring new ideas and technologies to stay at the forefront of our field.
- **Community**: We value our community and aim to create a supportive and engaging environment for all our members.

## Join Us

We invite you to join our community and embark on this learning journey with us. Whether you're a seasoned developer, a student, or just someone with a keen interest in AI and technology, there's something for everyone here at [Your Website Name].

Thank you for visiting, and we look forward to connecting with you!

Best regards,  
[Your Name]  
Founder, [Your Website Name]

---

## Contact Information

For any inquiries or feedback, please visit our [Contact Page](link to contact page).

""")
