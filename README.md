# Fake News Detection using Logistic Regression

This project detects whether a given news article is **Fake** or **Real** using a machine learning model trained with **Logistic Regression** and deployed using **Streamlit**.

## 🔍 Features
- Preprocessing & TF-IDF vectorization
- Model training and evaluation (Accuracy ~99%)
- Classifier comparison (SVM, Naive Bayes, Neural Net)
- Deployed web app for live predictions

## 🚀 Try the App
👉 [Click here to view the app](https://fake-news-detector-ensknseqzfvcv8p87pgvo4.streamlit.app/)

## 📁 Files
- `app.py` — Streamlit frontend
- `logistic_model.pkl` — Trained classifier
- `tfidf_vectorizer.pkl` — TF-IDF feature transformer
- `requirements.txt` — Dependencies

## 📊 Sample Input
> "NASA successfully launches Artemis mission to the moon."

→ Output: ✅ Real News

## 📚 References
- Used dataset: [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data)
- Literature survey: Based on 4 published papers
