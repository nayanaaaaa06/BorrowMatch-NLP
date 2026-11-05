
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load the NLP model
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_items():
    """Load available borrowing items from the database."""
    return pd.read_csv("borrow_items.csv")


def recommend_items(user_query, top_k=5):
    """Find items semantically similar to the user's request."""

    items = load_items()

    if items.empty:
        return pd.DataFrame()

    descriptions = (
        items["item_name"].fillna("") + " " +
        items["category"].fillna("") + " " +
        items["description"].fillna("")
    ).tolist()

    item_embeddings = model.encode(
        descriptions, convert_to_tensor=True
    )

    query_embedding = model.encode(
        user_query, convert_to_tensor=True
    )

    scores = util.cos_sim(
        query_embedding, item_embeddings
    )[0]

    top_indices = scores.argsort(descending=True)[:top_k]

    results = items.iloc[top_indices.cpu().numpy()].copy()
    results["similarity_score"] = [
        round(scores[i].item() * 100, 2)
        for i in top_indices
    ]

    return results.sort_values(
        by="similarity_score", ascending=False
    ).reset_index(drop=True)
