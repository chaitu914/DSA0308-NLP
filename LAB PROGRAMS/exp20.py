from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
documents = [
    "Python is a programming language",
    "Python is used for machine learning",
    "Machine learning is a part of artificial intelligence",
    "Artificial intelligence uses machine learning"
]

# User query
query = "Python machine learning"

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

# Calculate cosine similarity
similarity = cosine_similarity(query_vector, doc_vectors)[0]

# Rank documents
ranking = similarity.argsort()[::-1]

print("Query:", query)
print("\nDocument Ranking:")

for i in ranking:
    print(f"Document {i+1}: Score = {similarity[i]:.4f}")
    print(documents[i])
    print()