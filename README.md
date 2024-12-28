# ML Movies Recommender System
## Play with app via url : https://ricky-ml-movies-recommender.streamlit.app/

## Overview

The ML Movies Recommender System is a machine learning-based application that recommends movies based on user input. By utilizing the power of cosine similarity and content-based filtering, the system suggests movies similar to the one the user selects.

This project includes a user interface built using **Streamlit**, which allows users to interact with the recommender system and see the results displayed in a visually appealing format, including movie posters.

## Features

- **Movie Recommendations**: Suggests movies based on the similarity of movie content (such as genres, tags, and keywords).
- **Movie Posters**: Displays movie posters for the recommended films.
- **Interactive UI**: Users can input a movie title and receive movie recommendations.
- **Efficient Recommender**: Built using content-based filtering and cosine similarity to generate recommendations.

## Technologies Used

- **Python**: The core programming language for building the recommendation system.
- **Streamlit**: Framework used for building the web interface.
- **Scikit-learn**: Used for machine learning model implementation and cosine similarity.
- **Joblib**: Used for saving and loading the model.
- **Pandas**: For data manipulation and preprocessing.
- **Requests**: To fetch movie posters using movie titles.
- **Heroku/Streamlit Cloud**: For deployment.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/ml-movies-recommender.git
cd ML-Movies-Recommender-App
