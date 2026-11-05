
import streamlit as st
import pandas as pd
from recommender import recommend_items

# Page configuration
st.set_page_config(
    page_title="BorrowMatch NLP",
    page_icon="📚",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #60A5FA;
}
.subtitle {
    font-size: 17px;
    color: #CBD5E1;
}
.item-card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">📚 BorrowMatch-NLP</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Campus Borrowing '
    'Recommendation System using Natural Language Processing</div>',
    unsafe_allow_html=True
)

st.divider()

# Load database
@st.cache_data
def load_data():
    return pd.read_csv("borrow_items.csv")

df = load_data()

# Sidebar
st.sidebar.title("🎯 Dashboard")

categories = ["All"] + sorted(df["category"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Filter by Category",
    categories
)

st.sidebar.markdown("---")
st.sidebar.info(
    "BorrowMatch uses semantic NLP to understand "
    "student requests and recommend relevant items."
)

# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Items", len(df))

with col2:
    st.metric(
        "Available Items",
        len(df[df["availability"] == "Available"])
    )

with col3:
    st.metric("Categories", df["category"].nunique())

st.divider()

# Search section
st.subheader("🔍 Find What You Need")

st.write(
    "Describe the item you want in normal language. "
    "Our NLP engine will find semantically similar items."
)

user_query = st.text_input(
    "What are you looking for?",
    placeholder="Example: I need a laptop for machine learning projects"
)

top_k = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("✨ Find Recommendations", type="primary"):

    if not user_query.strip():
        st.warning("Please enter what you are looking for.")

    else:
        with st.spinner("Understanding your request..."):

            results = recommend_items(user_query, top_k)

            if selected_category != "All":
                results = results[
                    results["category"] == selected_category
                ]

            results = results[
                results["availability"] == "Available"
            ]

        st.subheader("🎯 Recommended Items")

        if results.empty:
            st.info("No matching available items found.")

        else:
            for _, item in results.iterrows():

                with st.container(border=True):

                    left, right = st.columns([3, 1])

                    with left:
                        st.markdown(
                            f"### 📦 {item['item_name']}"
                        )

                        st.write(
                            f"**Category:** {item['category']}"
                        )

                        st.write(
                            f"**Description:** {item['description']}"
                        )

                        st.write(
                            f"**Condition:** {item['condition']}"
                        )

                        st.write(
                            f"**Owner:** {item['owner']}"
                        )

                    with right:
                        st.metric(
                            "Similarity",
                            f"{item['similarity_score']}%"
                        )

                        st.success(item["availability"])

                        st.caption(
                            f"Item ID: {item['item_id']}"
                        )

st.divider()

# Browse all items
st.subheader("📖 Browse Campus Items")

if selected_category == "All":
    display_df = df
else:
    display_df = df[df["category"] == selected_category]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")
st.caption(
    "BorrowMatch-NLP | AI & ML Project | "
    "Semantic Search using Sentence Transformers"
)
