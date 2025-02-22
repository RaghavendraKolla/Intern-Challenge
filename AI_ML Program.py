import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def load_dataset(filepath):
    """Loads a dataset containing items with textual descriptions."""
    return pd.read_csv(filepath)

def preprocess_text(data, text_column):
    """Converts text data into TF-IDF vectors with additional preprocessing."""
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))  # Using unigrams and bigrams
    tfidf_matrix = vectorizer.fit_transform(data[text_column])
    return vectorizer, tfidf_matrix

def filter_by_genre(data, genre):
    """Filters the dataset by genre using keyword matching in descriptions."""
    genre_keywords = {
    'action': ['action', 'explosion', 'chase', 'fight', 'battle', 'hero', 'combat', 'war', 'adventure', 'explosions'],
    'thriller': ['thriller', 'suspense', 'mystery', 'intense', 'cliffhanger', 'nervous', 'murder', 'crime', 'investigation', 'danger'],
    'comedy': ['comedy', 'funny', 'laugh', 'humor', 'joke', 'comedian', 'parody', 'satire', 'spoof', 'stand-up'],
    'horror': ['horror', 'scary', 'frightening', 'ghost', 'monster', 'spooky', 'zombie', 'blood', 'murder', 'creepy'],
    'romance': ['romance', 'love', 'heart', 'couple', 'relationship', 'passion', 'date', 'affection', 'kiss', 'emotions'],
    'drama': ['drama', 'emotional', 'intense', 'tragic', 'serious', 'conflict', 'life', 'love story', 'family', 'heartfelt'],
    'fantasy': ['fantasy', 'magic', 'wizard', 'dragon', 'mystical', 'fairy tale', 'quest', 'supernatural', 'kingdom', 'myth'],
    'adventure': ['adventure', 'journey', 'exploration', 'quest', 'discovery', 'treasure', 'explorer', 'dangerous', 'survival', 'wild'],
    'animation': ['animation', 'animated', 'cartoon', 'CGI', '2D', '3D', 'kids', 'family', 'animated series', 'cartoons'],
    'documentary': ['documentary', 'true story', 'real life', 'non-fiction', 'biography', 'historical', 'investigation', 'reportage', 'interview'],
    
}

    
    # Combine all genre keywords into one list
    keywords = genre_keywords.get(genre.lower(), [])
    
    if keywords:
        # Use regex for more flexible matching to capture multiple forms of words (e.g., comedian, comedy)
        genre_filtered_data = data[data['description'].str.contains('|'.join(keywords), case=False, na=False)]
        
        # Check if the filtered data is empty
        if genre_filtered_data.empty:
            print(f"No movies found with genre '{genre}' in the descriptions.")
            return data  # Return the entire dataset if no matches are found
        return genre_filtered_data
    else:
        return data  # No filtering if no matching genre is found

def get_recommendations(user_input, vectorizer, tfidf_matrix, data, genre=None, top_n=5):
    """Finds the top N similar items based on cosine similarity, with optional genre filtering."""
    # Filter by genre if provided
    if genre:
        data = filter_by_genre(data, genre)
        tfidf_matrix = vectorizer.transform(data['description'])  # Recompute TF-IDF matrix for filtered data
    
    # Compute cosine similarity with user input
    user_tfidf = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    # Sort the movies by similarity score
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    
    # Return the top recommendations with similarity scores
    recommendations = data.iloc[top_indices][['title', 'description']]
    recommendations['similarity_score'] = similarity_scores[top_indices]
    return recommendations

def main():
    """Runs the recommendation system based on user input."""
    dataset_path = '/movies.csv'  # Replace with actual dataset path
    data = load_dataset(dataset_path)
    
    # Preprocess movie descriptions to create TF-IDF vectors
    vectorizer, tfidf_matrix = preprocess_text(data, 'description')
    
    # Get user input for genre and description
    # genre = input("Enter the genre (e.g., Action, Thriller, Comedy, Horror, Romance, Drama, Adventure, Animation, Documentry, Fantasy): ").strip()
    user_input = input("Enter a description of the type of movies you like: ").strip()
    
    # Get movie recommendations
    recommendations = get_recommendations(user_input, vectorizer, tfidf_matrix, data, top_n=5)
    
    # Display top recommendations with similarity scores
    print("\nTop Recommendations:")
    for idx, row in recommendations.iterrows():
        print(f"Title: {row['title']}\nDescription: {row['description']}\nSimilarity Score: {row['similarity_score']:.3f}\n")

if __name__ == "__main__":
    main()
