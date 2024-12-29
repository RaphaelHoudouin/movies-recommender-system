# Streamlit app title and subheading - Centered with custom CSS
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .subheading {
        text-align: center;
        color: lightgray;
        margin-top: -10px; /* Negative margin to bring the subheading closer */
        margin-bottom: 30px; /* Increased space below the subheading */
    }
    .instructions {
        margin-bottom: -10px; /* Reduce space after instructions */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.markdown('<p class="title">REEL IT IN 🎬</p>', unsafe_allow_html=True)

# Centered subheading for the app with light grey color and added space
st.markdown('<h3 class="subheading">Movies Recommender</h3>', unsafe_allow_html=True)

# Instructions for the user
st.markdown("""
    Select or type a movie you like, and get similar movie recommendations.
    Enjoy discovering new films! 🍿
""", unsafe_allow_html=True)

# Add space after the text using CSS styling
st.markdown("<style>div.stSelectbox { margin-top: 20px; }</style>", unsafe_allow_html=True)

