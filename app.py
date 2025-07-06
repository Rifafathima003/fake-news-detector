
import streamlit as st
import pickle

# Load model and vectorizer
try:
    model = pickle.load(open("logistic_model.pkl", "rb"))
    vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
except FileNotFoundError:
    st.error("Model or vectorizer file not found. Make sure both .pkl files are in the same directory as app.py")
    st.stop()

# Title and input
st.title("Fake News Detector")
user_input = st.text_area("Enter a news article text below:")

if st.button("Check if it's Fake or Real"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform input and predict
        x_input = vectorizer.transform([user_input])
        prediction = model.predict(x_input)[0]
        label = "Fake News" if prediction == 1 else "Real News"
        st.success(f"The article is classified as: {label}")
