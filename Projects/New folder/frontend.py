import streamlit as st
import joblib
from pathlib import Path

# Absolute path of the folder containing frontend.py
BASE_DIR = Path(__file__).parent

# Load models
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")
svm_model = joblib.load(BASE_DIR / "svm_intent_classifier.pkl")

# -----------------------------
# Prediction function
# -----------------------------
def predict_intent(query):
    query_vector = vectorizer.transform([query])

    prediction = svm_model.predict(query_vector)[0]

    confidence = svm_model.decision_function(query_vector).max()

    return prediction, confidence

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Banking Intent Classifier",
    page_icon="🏦",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🏦 Banking Intent Classifier")
st.markdown(
    """
    Detect the intent of a customer banking query using a **TF-IDF + Linear SVM** model.
    """
)

# -----------------------------
# Input
# -----------------------------
query = st.text_area(
    "Enter Customer Query",
    placeholder="Example: My card has not arrived yet",
    height=150
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Intent", use_container_width=True):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:

        intent, score = predict_intent(query)

        st.success("Prediction Complete")

        st.markdown("## 🎯 Predicted Intent")
        st.info(intent)

        st.metric("Decision Score", f"{score:.2f}")
        st.caption("Higher values indicate the query is farther from competing classes. This is not a probability.")    

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Model: TF-IDF + Linear SVM | Banking77 Dataset")