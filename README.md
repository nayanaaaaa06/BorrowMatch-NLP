# BorrowMatch-NLP 📚

### Smart Campus Borrowing Recommendation System using Natural Language Processing

## 📌 Project Overview
BorrowMatch-NLP is an AI-powered campus borrowing recommendation system that helps students find relevant items using natural language queries.

Instead of searching using exact keywords, students can describe what they need in normal language. The system uses Natural Language Processing (NLP) and Sentence Transformers to identify semantically similar items.

## 🎯 Objectives
- Develop an intelligent campus item recommendation system.
- Implement semantic search using NLP.
- Compare TF-IDF and Sentence Transformer approaches.
- Recommend relevant items based on user queries.
- Display item availability and details.

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- Sentence Transformers
- TF-IDF
- Cosine Similarity

## ⚙️ Features
1. Interactive dashboard.
2. Campus item browsing.
3. Category-based filtering.
4. Natural language search.
5. Semantic item recommendations.
6. Similarity score display.
7. Item availability information.
8. Model evaluation using TF-IDF and Semantic NLP.

## 🧠 NLP Model
The project uses the pre-trained Sentence Transformer model:

`all-MiniLM-L6-v2`

Cosine similarity is used to calculate the similarity between student queries and campus item descriptions.

## 📊 Model Evaluation

The model was evaluated using five sample student queries.

| Evaluation Method | Average Similarity |
|---|---:|
| TF-IDF | 54.97% |
| Semantic NLP | 68.11% |

The evaluation indicates that Semantic NLP achieved a higher average similarity score on the selected sample queries.

## 📁 Project Structure

```text
BorrowMatch-NLP/
│
├── app.py
├── recommender.py
├── generate_database.py
├── evaluate.py
├── borrow_items.csv
├── evaluation_results.csv
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project

1. Clone or download the repository.
2. Open the project folder in VS Code.
3. Create and activate a Python virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
streamlit run app.py
```

6. Open the local URL displayed in the terminal.

## 📈 Evaluation

Run the evaluation script:

```bash
python evaluate.py
```

The program compares TF-IDF and Semantic NLP similarity scores and generates `evaluation_results.csv`.

## 🔮 Future Enhancements
- Student login and registration.
- Borrowing request management.
- Real-time item availability updates.
- Admin dashboard.
- Improved recommendation accuracy using larger datasets.

## 👩‍💻 Project
**BorrowMatch-NLP – AI & ML Project**

*Semantic Search using Sentence Transformers*
