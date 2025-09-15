import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

# =========================================================
# 1) CONTENT-BASED RECOMMENDATION
# =========================================================

# --- Sample movie dataset ---
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'John Wick', 'Inception', 'Toy Story', 'Finding Nemo'],
    'genres': ['Action Sci-Fi', 'Action Thriller', 'Action Sci-Fi', 'Animation Comedy', 'Animation Family']
})

# --- Convert genres into TF-IDF features ---
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# --- Compute similarity matrix between all movies ---
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# --- Recommendation function (Content-Based) ---
def recommend_content_based(title, cosine_sim=cosine_sim):
    if title not in movies['title'].values:
        return ["Movie not found!"]
    idx = movies.index[movies['title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Top 3 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()


# =========================================================
# 2) COLLABORATIVE FILTERING RECOMMENDATION
# =========================================================

# --- Sample user ratings dataset ---
ratings = pd.DataFrame({
    'user': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
    'movie': ['The Matrix', 'John Wick', 'The Matrix', 'Inception', 'John Wick', 'Toy Story'],
    'rating': [5, 4, 4, 5, 5, 3]
})

# --- Create User-Item Matrix ---
user_movie_matrix = ratings.pivot_table(index='user', columns='movie', values='rating')
user_movie_matrix = user_movie_matrix.fillna(0)

# --- Compute similarity between users ---
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# --- Recommendation function (Collaborative Filtering) ---
def recommend_collaborative(user):
    if user not in user_movie_matrix.index:
        return ["User not found!"]
    # Find most similar user
    similar_user = user_similarity_df[user].sort_values(ascending=False).index[1]
    # Find movies similar user liked but current user hasn't rated
    user_seen = user_movie_matrix.loc[user]
    similar_user_ratings = user_movie_matrix.loc[similar_user]
    recommendations = similar_user_ratings[(similar_user_ratings > 0) & (user_seen == 0)]
    return recommendations.sort_values(ascending=False).index.tolist()


# =========================================================
# 3) RUN DEMO
# =========================================================

if __name__ == "__main__":
    print("=== CONTENT-BASED RECOMMENDATION ===")
    print("Movies similar to 'The Matrix':")
    print(recommend_content_based("The Matrix"))

    print("\n=== COLLABORATIVE FILTERING RECOMMENDATION ===")
    print("Recommendations for Alice:")
    print(recommend_collaborative("Alice"))
