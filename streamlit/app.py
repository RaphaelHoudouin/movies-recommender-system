import streamlit as st
import os
import random  # Make sure to import the random module
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Ensure these helper functions are available

# Load model and data
load_data = load("artifacts/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

# Get movie titles
input_data = dataframe['original_title'].values

# Streamlit app title and subheading - Centered with custom CSS
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 35px;
    }
    .subheading {
        text-align: center;
        color: lightgray;
        margin-top: -20px; /* Negative margin to bring the subheading closer */
        margin-bottom: 35px; /* Increased space below the subheading */
    }
    .instructions {
        margin-bottom: -10px; /* Reduce space after instructions */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# List of available music files in the 'musics' folder
music_files = [
    'Johann Strauss II - The Blue Danube.mp3',
    'Dmitri Shostakovich - Walzer Nr 2.mp3',
    'Johannes Brahms - Hungarian Dance no. 5.mp3',
    'Richard Wagner - Ride of the Valkyries.mp3'
]

# Estimated durations of the music (in seconds)
music_durations = {
    'Johann Strauss II - The Blue Danube.mp3': 460,  # Example: 7 minutes and 40 seconds
    'Dmitri Shostakovich - Walzer Nr 2.mp3': 300,   # Example: 5 minutes
    'Johannes Brahms - Hungarian Dance no. 5.mp3': 210,  # Example: 3 minutes and 30 seconds
    'Richard Wagner - Ride of the Valkyries.mp3': 370,  # Example: 6 minutes and 10 seconds
}

# Function to play the music
def play_music(music_file):
    music_path = os.path.join('streamlit', 'musics', music_file)
    if os.path.exists(music_path):
        st.audio(music_path, start_time=0)
        duration = music_durations.get(music_file, 0)
        time.sleep(duration)  # Wait for the music to finish
        return True
    else:
        st.error(f"File not found: {music_file}")
        return False

# Select a random music file
selected_music = random.choice(music_files)

# Play the first music
if play_music(selected_music):
    # After the first music ends, play the next one
    st.write("Changing music...")
    time.sleep(2)  # A short pause before switching to the next music
    selected_music = random.choice(music_files)  # Select a new random music
    play_music(selected_music)  # Play the next music

# Construire le chemin relatif vers le fichier sélectionné
music_file = os.path.join('streamlit', 'musics', selected_music)

# Vérifier si le fichier existe
if not os.path.exists(music_file):
    st.error(f"File not found: {music_file}")
else:
    # Ajouter des informations non-cliquables au-dessus du lecteur audio
    st.write('<p style="font-size:20px;">🎵 Play Music
    
    # Jouer automatiquement la musique lorsque l'app s'ouvre
    st.audio(music_file, start_time=0)

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
