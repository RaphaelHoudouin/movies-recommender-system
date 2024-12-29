import streamlit as st
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Only import helper functions

# Load model and data
try:
    load_data = load("artifacts/save_model.joblib")
    dataframe = load_data['dataframe']
    similarity = load_data['similarity']
except Exception as e:
    st.error(f"Error loading model or data: {e}")

# Get movie titles
input_data = dataframe['original_title'].values

# Streamlit app title
st.title('REEL IT IN 🎬')

# Refined instructions with clearer steps
st.write("""
### How it works:
1. Choose or type a movie you like.
2. The app will recommend similar movies based on your choice.

Enjoy discovering new films! 🍿
""")

# Dropdown for movie input
select_input = st.selectbox("Select a movie from the list", [""] + input_data)

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

# Show loading spinner while fetching recommendations
if st.button("Get Similar Movie Suggestions"):
    with st.spinner("Fetching movie recommendations..."):
        if select_input:
            # Get recommendations
            recommended_movies = recommend(select_input)
            st.markdown("### Recommended Movies:")

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

# Credits at the bottom of the main page with an enhanced call-to-action
st.markdown("""
    ---
    **Developed by [rhoudouin](https://github.com/rhoudouin).**  
    For inquiries or feedback, feel free to visit the [GitHub profile](https://github.com/rhoudouin).
""")


