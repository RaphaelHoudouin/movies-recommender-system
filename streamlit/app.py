import streamlit as st
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Only import helper functions

# Load model and data
load_data = load("artifacts/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

# Get movie titles
input_data = dataframe['original_title'].values

# Streamlit app title - Centered with custom CSS
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.markdown('<p class="title">REEL IT IN 🎬</p>', unsafe_allow_html=True)

# Centered subheading for the app with light grey color
st.markdown('<h3 style="text-align: center; color: lightgray;">Movie Recommender App</h3>', unsafe_allow_html=True)


# Instructions for the user
st.markdown("""
    Select or type a movie you like, and get similar movie recommendations.
    Enjoy discovering new films! 🍿
""", unsafe_allow_html=True)

# Add space after the text using CSS styling
st.markdown("<style>div.stSelectbox { margin-top: 20px; }</style>", unsafe_allow_html=True)

# Dropdown for movie input with searchable feature
select_input = st.selectbox(
    "Choose a movie:",
    [""] + input_data,
    key="movie_select"
)

# Add a loading spinner during recommendation processing
if st.button("Get Similar Movie Suggestions"):
    if select_input:
        with st.spinner('Fetching recommendations...'):
            # Get recommendations
            recommended_movies = recommend(select_input)
            st.markdown("**Recommended Movies:**")

            # Display movies with posters (3 per row)
            cols = st.columns(3)  # Create 3 columns
            for i, movie in enumerate(recommended_movies):
                with cols[i % 3]:  # Loop through columns
                    poster_url = fetch_movie_poster(movie)  # Fetch poster
                    st.image(poster_url, caption=movie, use_column_width=True)

                # Create new rows every 3 movies
                if (i + 1) % 3 == 0 and i != len(recommended_movies) - 1:
                    cols = st.columns(3)  # Create a new set of 3 columns
    else:
        st.warning("Please select a movie to get recommendations.")

# Credits at the bottom of the main page
st.markdown("""
    ---
    **Developed by [rhoudouin](https://github.com/rhoudouin).**  
    For inquiries or feedback, feel free to visit the GitHub profile.
""")

