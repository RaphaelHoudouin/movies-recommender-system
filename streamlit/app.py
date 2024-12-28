import streamlit as st
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Only import helper functions

# Load model and data
load_data = load("artifact/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

# Get movie titles
input_data = dataframe['original_title'].values

# Streamlit app title
st.title('Movies Recommender')

# Dropdown for movie input
select_input = st.selectbox("Input any film", [""] + input_data)

# Custom button style
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Generate recommendations
if st.button("Get Similar Movie Suggestions"):
    if select_input:
        # Get recommendations
        recommended_movies = recommend(select_input)
        st.markdown("Recommended Movies:")

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
