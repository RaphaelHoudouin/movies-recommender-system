import streamlit as st
import os
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Ensure these helper functions are available

# Load model and data
load_data = load("artifacts/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

# Get movie titles
input_data = dataframe['original_title'].values

# Function for displaying the music player with a single track
def display_music_player():
    music_file = os.path.join('streamlit', 'musics', 'Johann Strauss II - The Blue Danube.mp3')

    if os.path.exists(music_file):
        st.write('<p style="font-size:20px; text-align:left;">🎵 Play Music</p>', unsafe_allow_html=True)
        st.audio(music_file, start_time=0)
    else:
        st.error(f"File not found: {music_file}")

# Function for displaying the movie recommendation
def display_movie_recommendations(recommended_movies):
    st.markdown("**Recommended Movies:**")

    if len(recommended_movies) == 0:
        st.warning("Sorry, no recommendations available.")
    else:
        # Display movies with posters (3 per row)
        cols = st.columns(3)  # Create 3 columns
        for i, movie in enumerate(recommended_movies):
            with cols[i % 3]:  # Loop through columns
                poster_url = fetch_movie_poster(movie)  # Fetch poster
                st.image(poster_url, caption=movie, use_column_width=True)

            # Create new rows every 3 movies
            if (i + 1) % 3 == 0 and i != len(recommended_movies) - 1:
                cols = st.columns(3)  # Create a new set of 3 columns

# Custom CSS for styling the app
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 40px;
    }
    .subheading {
        text-align: center;
        color: lightgray;
        margin-top: -20px;
        margin-bottom: 35px;
    }
    .instructions {
        margin-bottom: -10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display music player
display_music_player()

# Centered title and subheading
st.markdown('<p class="title">REEL IT IN 🎬</p>', unsafe_allow_html=True)
st.markdown('<h3 class="subheading">Movies Recommender</h3>', unsafe_allow_html=True)

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
            display_movie_recommendations(recommended_movies)
    else:
        st.warning("Please select a movie to get recommendations.")

# Credits at the bottom of the main page
st.markdown("""
    ---
    **Developed by [raphaelhoudouin](https://github.com/raphaelhoudouin).**   
    For inquiries or feedback, feel free to visit the GitHub profile.
""")
