# Function to display a card with custom styling
def card(title, text, image, url, styles):
    return f"""
    <div class="card-container">
        <a href="{url}" class="card">
            <img src="{image}" alt="Card image">
            <div class="card-title">{title}</div>
            <div class="card-text">{text}</div>
        </a>
    </div>
    """


# Example usage of the card function to create multiple cards
cards = [
    card(
        title="Skill I need",
        text="What is the skills I need for this job position?",
        image="https://images.pexels.com/photos/4348403/pexels-photo-4348403.jpeg?auto=compress&cs=tinysrgb&w=600",
        url="https://strathmorekonectikaaiapp.streamlit.app/job_chat/?jobID=data_entry_clerk_001&prompt=what%20skills%20do%20I%20need%20for%20this%20job%3F",
        styles="border"
    ),
    card(
        title="What is this job about?",
        text="What will be my role doing this job?",
        image="https://images.pexels.com/photos/20875710/pexels-photo-20875710/free-photo-of-what-made-of-wooden-letters.jpeg?auto=compress&cs=tinysrgb&w=600",
        url="https://strathmorekonectikaaiapp.streamlit.app/job_chat/?jobID=data_entry_clerk_001&prompt=what%20is%20this%20job%20about",
        styles="border"
    ),
    card(
        title="Why This Job?",
        text="What are the importance of this job to me?",
        image="https://images.pexels.com/photos/12347774/pexels-photo-12347774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        url="https://strathmorekonectikaaiapp.streamlit.app/job_chat/?jobID=data_entry_clerk_001&prompt=why%20this%20job%3F",
        styles="border"
    ),
    # Add more cards as needed
]


def create_cards(st):

    # CSS to display cards in a row
    st.markdown(
        """    <style>
    .card-container {
        width: 100%;
        text-align: center;
        margin: 20px;
    }
    .card {
        display: block;
        height:100%;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-decoration: none;
        color: inherit;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.2);
    }
    .card img {
        border-radius: 10px;
        max-width: 100%;
        height: auto;
    }
    .card-title {
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    .card-text {
        font-size: 16px;
        color: #666;
        margin: 10px 0;
    }
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
        justify-items: center;
    }
    </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card-row">', unsafe_allow_html=True)
        st.markdown(cards[0], unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-row">', unsafe_allow_html=True)
        st.markdown(cards[1], unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card-row">', unsafe_allow_html=True)
        st.markdown(cards[2], unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Display the cards in a row
    # st.markdown('<div class="card-row">', unsafe_allow_html=True)
    # for card_html in cards:
    #     st.markdown(card_html, unsafe_allow_html=True)
    # st.markdown('</div>', unsafe_allow_html=True)
