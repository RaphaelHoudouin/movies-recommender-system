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
        border-radius



