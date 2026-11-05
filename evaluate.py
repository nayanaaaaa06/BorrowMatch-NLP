
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load dataset
df = pd.read_csv("borrow_items.csv")

# Combine item details
documents = (
    df["item_name"].fillna("") + " " +
    df["category"].fillna("") + " " +
    df["description"].fillna("")
).tolist()

# Sample student queries
queries = [
    "I need a laptop for Python programming",
    "Looking for books about artificial intelligence",
    "I want something for engineering drawing",
    "Need headphones for online classes",
    "I need a device to store my project files"
]

# Method 1: TF-IDF keyword-based retrieval
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

# Method 2: Semantic NLP retrieval
model = SentenceTransformer("all-MiniLM-L6-v2")
item_embeddings = model.encode(documents, convert_to_tensor=True)

tfidf_scores = []
semantic_scores = []

for query in queries:

    # TF-IDF
    query_vector = tfidf.transform([query])
    scores = cosine_similarity(query_vector, tfidf_matrix)[0]
    tfidf_scores.append(max(scores))

    # Semantic similarity
    query_embedding = model.encode(
        query, convert_to_tensor=True
    )
    similarities = util.cos_sim(
        query_embedding, item_embeddings
    )[0]
    semantic_scores.append(float(similarities.max()))

# Results
print("\n========== MODEL EVALUATION ==========")

print("\nTF-IDF Average Similarity:",
      round(sum(tfidf_scores) / len(tfidf_scores) * 100, 2), "%")

print("Semantic NLP Average Similarity:",
      round(sum(semantic_scores) / len(semantic_scores) * 100, 2), "%")

results = pd.DataFrame({
    "Query": queries,
    "TF-IDF Score": [round(x * 100, 2) for x in tfidf_scores],
    "Semantic NLP Score": [round(x * 100, 2) for x in semantic_scores]
})

print("\nDetailed Results:")
print(results.to_string(index=False))

results.to_csv("evaluation_results.csv", index=False)

print("\nEvaluation completed successfully!")
