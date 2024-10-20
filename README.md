# Music Recommendation System 🎶

This is a Flask-based web application that recommends music based on a given song. The system uses **TF-IDF Vectorization** and **Cosine Similarity** to provide song recommendations from a pre-trained model.

## Features

- **Song Recommendations**: Based on a song input, it suggests 5 similar songs(Specifically made for Holluwood songs).
- **Auto-complete Suggestions**: While typing a song name, the system provides auto-suggestions.
- **Simple User Interface**: A clean and intuitive web page where users can search for songs and get recommendations.
  

## Technologies Used

1. **Python**: Core programming language for building the backend logic.
2. **Flask**: Lightweight web framework for developing the web application.
3. **HTML5 & CSS3**: For designing the user interface of the web application.
4. **JavaScript (ES6)**: Used for handling the auto-suggestions feature and asynchronous API calls.
5. **Pickle**: To serialize and load the pre-trained music recommendation model.
6. **TF-IDF Vectorizer**: For vectorizing the song data to compute text similarity.
7. **Cosine Similarity**: To measure similarity between the input song and others for recommendation.


## Usage

1. Enter a song name or genre in the search bar.
2. The system will auto-suggest possible matches as you type.
3. Submit the form to get a list of recommended songs similar to your input.

## License

This project is licensed under the MIT License.


