import streamlit as st
import os
import random  # Assurez-vous d'importer le module random
from joblib import load
from db_helper import recommend, fetch_movie_poster  # Assurez-vous que ces fonctions sont disponibles

# Charger le modèle et les données
load_data = load("artifacts/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

# Obtenir les titres des films
input_data = dataframe['original_title'].values

# Titre et sous-titre de l'application Streamlit - Centré avec CSS personnalisé
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
        margin-top: -20px; /* Marges négatives pour rapprocher le sous-titre */
        margin-bottom: 35px; /* Espacement accru sous le sous-titre */
    }
    .instructions {
        margin-bottom: -10px; /* Réduire l'espace après les instructions */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Liste des fichiers musicaux disponibles dans le dossier 'musics'
music_files = [
    'Johann Strauss II - The Blue Danube.mp3',
    'Dmitri Shostakovich - Walzer Nr 2.mp3',
    'Johannes Brahms - Hungarian Dance no. 5.mp3',
    'Richard Wagner - Ride of the Valkyries.mp3'
]

# Sélectionner un fichier musical aléatoire
selected_music = random.choice(music_files)

# Construire le chemin relatif vers le fichier sélectionné
music_file = os.path.join('streamlit', 'musics', selected_music)

# Vérifier si le fichier existe
if not os.path.exists(music_file):
    st.error(f"File not found: {music_file}")
else:
    # Jouer automatiquement la musique lorsque l'app s'ouvre, sans afficher le titre
    st.audio(music_file, start_time=0)

 # Ajouter des informations non-cliquables au-dessus du lecteur audio
    st.write('<p style="font-size:20px;">🎵 Play Music

# Titre centré
st.markdown('<p class="title">REEL IT IN 🎬</p>', unsafe_allow_html=True)

# Sous-titre centré pour l'application avec une couleur gris clair et espace ajouté
st.markdown('<h3 class="subheading">Movies Recommender</h3>', unsafe_allow_html=True)

# Instructions pour l'utilisateur
st.markdown("""
    Select or type a movie you like, and get similar movie recommendations.
    Enjoy discovering new films! 🍿
""", unsafe_allow_html=True)

# Ajouter de l'espace après le texte avec un style CSS
st.markdown("<style>div.stSelectbox { margin-top: 20px; }</style>", unsafe_allow_html=True)

# Menu déroulant pour l'entrée du film avec fonctionnalité de recherche
select_input = st.selectbox(
    "Choose a movie:",
    [""] + input_data,
    key="movie_select"
)

# Ajouter un spinner pendant le traitement des recommandations
if st.button("Get Similar Movie Suggestions"):
    if select_input:
        with st.spinner('Fetching recommendations...'):
            # Obtenir les recommandations
            recommended_movies = recommend(select_input)
            st.markdown("**Recommended Movies:**")

            # Afficher les films avec leurs affiches (3 par ligne)
            cols = st.columns(3)  # Créer 3 colonnes
            for i, movie in enumerate(recommended_movies):
                with cols[i % 3]:  # Boucle à travers les colonnes
                    poster_url = fetch_movie_poster(movie)  # Récupérer l'affiche
                    st.image(poster_url, caption=movie, use_column_width=True)

                # Créer de nouvelles lignes après chaque 3 films
                if (i + 1) % 3 == 0 and i != len(recommended_movies) - 1:
                    cols = st.columns(3)  # Créer un nouveau set de 3 colonnes
    else:
        st.warning("Please select a movie to get recommendations.")

# Crédits au bas de la page principale
st.markdown("""
    ---
    **Developed by [rhoudouin](https://github.com/rhoudouin).**  
    For inquiries or feedback, feel free to visit the GitHub profile.
""")


