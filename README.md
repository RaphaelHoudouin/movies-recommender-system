# ML Movies Recommender System

## Table of Contents
- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Usage and Configuration](#usage-and-configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project

The **ML Movies Recommender System** is a machine learning-based application that recommends movies based on user input. By utilizing the power of cosine similarity and content-based filtering, the system suggests movies similar to the one the user selects. This project includes a user interface built using **Streamlit**, which allows users to interact with the recommender system and see the results displayed in a visually appealing format, including movie posters.

### Dataset

The system is powered by the **tmdb_5000_movies.csv** dataset, which is sourced from the Kaggle dataset:  
[TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).  
This dataset contains metadata for 5000 movies, including details such as genres, tags, keywords, and more.

This project includes a user interface built using **Streamlit**, which allows users to interact with the recommender system and see the results displayed in a visually appealing format, including movie posters.

### Live App
Explore the app via this URL: [ML Movies Recommender](https://ricky-ml-movies-recommender.streamlit.app/).

## Key Features

1. **Movie Recommendations:**
   - Suggests movies based on the similarity of movie content (such as genres, tags, and keywords).

2. **Movie Posters:**
   - Displays movie posters for the recommended films.

3. **Interactive UI:**
   - Users can input a movie title and receive movie recommendations.

4. **Efficient Recommender:**
   - Built using content-based filtering and cosine similarity to generate recommendations.

## Technology Stack

- **Machine Learning:** Scikit-learn (for cosine similarity)
- **Web Framework:** Streamlit
- **Model Persistence:** Joblib (for saving and loading models)
- **Data Processing:** Pandas
- **Web Requests:** Requests (for fetching movie posters)
- **Deployment:** Heroku/Streamlit Cloud

## Getting Started

To get started with this project locally, you’ll need Python 3.8+ installed on your machine along with some necessary Python packages. You can either clone the repository and install dependencies manually or use Docker for an isolated environment.

### Installation Steps

#### Option 1: Installation from GitHub

1. Clone the repository:
   ```bash
   git clone https://github.com/rhoudouin/movies-recommender-system.git

## License

Distributed under the GNU General Public License (GPL). See LICENSE for more information.


## Acknowledgements

- **Scikit-learn:** For providing machine learning algorithms and utilities.
- **Streamlit:** For creating the interactive web application.
- **NumPy & Pandas:** For preprocessing and numerical computation.
- **Joblib:** For model serialization and deployment.
- **Kaggle**: For accessing diverse datasets to power machine learning projects.

## Contact

For any questions or feedback, please contact the project maintainer: **rhoudouin**  
GitHub: [rhoudouin](https://github.com/rhoudouin)




