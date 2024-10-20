from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load the saved model (TF-IDF, cosine similarity, indices, and music data)
with open('music_recommendation_model.pkl', 'rb') as model_file:
    tfidf, cosine_sim, indices, music_data = pickle.load(model_file)

# Load the song names from a text file
def load_song_names():
    song_file = os.path.join(os.getcwd(), 'songs.txt')
    if os.path.exists(song_file):
        with open(song_file, 'r') as f:
            songs = [line.strip() for line in f.readlines()]
        return songs    
    return []

# Function to get song recommendations
def get_recommendations(song_name):
    if song_name not in indices:
        raise ValueError("Sorry, song not found")
    
    idx = indices[song_name]  # Get the index of the song in the dataset
    sim_scores = list(enumerate(cosine_sim[idx]))  # Get pairwise similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Sort by similarity
    sim_scores = sim_scores[1:6]  # Get top 5 similar songs
    
    # Get the song indices for the top recommendations
    song_indices = [i[0] for i in sim_scores]
    
    # Return the actual song names
    return music_data['Song-Name'].iloc[song_indices].tolist()

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    song_name = request.form['song_name']
    try:
        recommendations = get_recommendations(song_name)
        return jsonify({'recommendations': recommendations})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error: ' + str(e)}), 500

# Route to serve song names for auto-suggestions
@app.route('/get-songs', methods=['GET'])
def get_songs():
    query = request.args.get('query', '').lower()
    all_songs = load_song_names()

    # Filter songs based on the search query (case insensitive)
    suggestions = [song for song in all_songs if query in song.lower()]
    
    print(f"Query: {query} | Suggestions: {suggestions}")  # Debugging: Check what's being returned
    
    if not suggestions:  # If there are no suggestions
        print("No suggestions found.")  # Debugging
    return jsonify(suggestions)  # Return the list of filtered songs as JSON

if __name__ == '__main__':
    app.run(debug=True)
