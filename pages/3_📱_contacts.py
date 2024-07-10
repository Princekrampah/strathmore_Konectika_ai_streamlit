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


st.title("Contacts")

st.markdown("""

# Contact Us

We'd love to hear from you! Whether you have a question about our content, feedback, or just want to say hello, feel free to reach out to us.

## Get in Touch

### Email
You can email us directly at: [contact@yourwebsite.com](mailto:contact@yourwebsite.com)

### Social Media
Follow and connect with us on our social media channels:

- **Twitter**: [@yourtwitterhandle](https://twitter.com/yourtwitterhandle)
- **Facebook**: [Your Facebook Page](https://facebook.com/yourfacebookpage)
- **Instagram**: [@yourinstagramhandle](https://instagram.com/yourinstagramhandle)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourlinkedinprofile)
- **YouTube**: [Your YouTube Channel](https://youtube.com/yourchannel)

### Mailing Address
If you prefer snail mail, you can reach us at:

""")
