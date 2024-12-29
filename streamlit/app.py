import streamlit as st
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Only import helper functions

# Chargement du modèle et des données
try:
    load_data = load("artifacts/save_model.joblib")
    dataframe = load_data['dataframe']
    similarity = load_data['similarity']
except Exception as e:
    st.error(f"Error loading model or data: {e}")

# Récupération des titres de films
input_data = dataframe['original_title'].values

# Titre de l'application
st.title('REEL IT IN 🎬')

# Instructions pour l'utilisateur
st.markdown("""
### How it works:
1. **Choose or type a movie you like**: Use the dropdown or type the movie name in the input box below.
2. **Get personalized recommendations**: Click the button to see similar movies based on your selection.

Enjoy discovering new films! 🍿
""")

# Zone de sélection et d'entrée de texte
col1, col2 = st.columns([3, 1])  # Crée deux colonnes pour une mise en page équilibrée
with col1:
    select_input = st.selectbox("Select a movie from the list:", [""] + input_data)
with col2:
    st.markdown("")

# Bouton personnalisé
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

# Récupération des recommandations
if st.button("Get Similar Movie Suggestions"):
    if select_input:
        with st.spinner("Fetching movie recommendations..."):
            # Appel des fonctions pour obtenir les recommandations
            recommended_movies = recommend(select_input)
            st.markdown("### Recommended Movies:")

            # Affichage des films avec les affiches (3 par ligne)
            cols = st.columns(3)  # Crée 3 colonnes
            for i, movie in enumerate(recommended_movies):
                with cols[i % 3]:  # Itère sur les colonnes
                    poster_url = fetch_movie_poster(movie)  # Récupère l'affiche
                    st.image(poster_url, caption=movie, use_column_width=True)

                # Ajoute une nouvelle ligne toutes les 3 colonnes
                if (i + 1) % 3 == 0 and i != len(recommended_movies) - 1:
                    cols = st.columns(3)  # Crée un nouveau set de colonnes
    else:
        st.warning("Please select a movie to get recommendations.")

# Crédits
st.markdown("""
    ---
    **Developed by [rhoudouin](https://github.com/rhoudouin).**  
    For inquiries or feedback, feel free to visit the GitHub profile.
""")

