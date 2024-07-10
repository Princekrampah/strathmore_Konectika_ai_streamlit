import streamlit as st

from llama_index.llms.mistralai import MistralAI
from llama_index.core.llms import ChatMessage
from decouple import config


# custom function imports
from utils.html_to_pdf import html_to_pdf_converter
from utils.ui.cards import create_cards

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

llm = MistralAI(api_key=config("MISTRAL_API_KEY"))


jobs_details = {
    "data_entry_clerk_001": """
        Xpand Legal Consulting LLC
        Data Entry Clerk
        United States

        Easy Apply
        About the role
        We have a 1 month contract available for a data entry project logging time sheet entries on behalf of a law firm. Once the contract expires, there could be opportunities to continue to support various legal cases with data entry or case management services.

        About us
        We are a small, but mighty startup in the legal administrative space. We provide administrative assistance to law firms handling cases, primarily in the mass tort and className action space. We work hard, but support work-life balance and are looking for a team member who is ready to grow with us long term.

        Who we are looking for
        This is an ideal role for a self-starter looking to get experience in the legal field. An interest in the law or legal matters will be helpful. We are looking for a self-lead individual that works well independently and alongside the team, communicates clearly and effectively, takes direction, learns quickly, is well organized, and pays high attention to detail. You are a leader who takes pride in a job well done.

        Required Skills
        High attention to detail
        Fast Learner
        Self Lead
        Strong communication skill
        Experience working at either a law firm or degree related to legal field a plus
        Job Type
        Contract

        Pay
        $20.00 per hour

        Expected hours
        30 – 40 per week

        Benefits
        Flexible schedule
        Schedule
        8 hour shift

        Work Location
        Remote
    """
}

# get query parameters
job_id = st.query_params.get_all("jobID")
user_prompt_query_param = st.query_params.get_all("prompt")

if len(job_id) == 0:
    st.warning("Please provide a job ID to get started.")
    st.write("#### Provide me the job ID to get started.")

job_id = job_id[0]

# Create question cards
create_cards(st=st)


def ai_mentor(user_query, job_id: str):

    job_description = jobs_details.get(job_id, None)

    if job_description is None:
        yield "### Provided job ID is invalid. Please provide a valid job ID."
        return

    messages = [
        ChatMessage(role="system",
                    content=(
                        "You are a helpful AI mentor designed to help students with job application. "
                        "Help answer their questions in a helpful and friendly manner. "
                        "Given the following job description, advice the student on "
                        "how to prepare for the interview when asked for. Do not answer "
                        "any question that does not relate to the job description provided to you.\n\n"
                        f"Job Description:\n {job_description}\n\n"
                        "Incase the student or user asks any question that does to relate to the job "
                        "description, kindly let them know in a kind and polite way that you are only "
                        "allowed to answer questions that relate to the job description."
                        "Do not provide any advice to the student unless asked to."
                    )),
        ChatMessage(role="user", content=user_query),
    ]
    resp = llm.stream_chat(messages)

    for r in resp:
        yield r.delta


try:
    # TODO: add async/await to this
    print("called...")
    # Add download capability here
    html_to_pdf_converter()
except Exception as e:
    print(e)


st.title("Hello, welcome to Strathmore KonecTika")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(ai_mentor(prompt, job_id))
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

else:
    # check user prompt in query
    if len(user_prompt_query_param) > 0:
        prompt = user_prompt_query_param[0]

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(ai_mentor(prompt, job_id))
        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
