# 🕵️‍♂️ Fake Job Posting Detection System

A machine learning-based Streamlit web app that detects whether a job posting is **REAL** or **FAKE** based on the job title and description. This project demonstrates the full data science workflow from raw dataset to a deployed web application.

---

## 📌 Problem Statement

Fake job listings are increasingly used for scams, phishing, and stealing personal data. Manually verifying job posts is time-consuming. This project aims to build an automated system that predicts if a job posting is real or fraudulent using natural language processing (NLP) and machine learning.

---

## 🎯 Objectives

- Preprocess job data and clean text
- Build a machine learning model to classify real vs fake jobs
- Build a frontend using Streamlit for user interaction
- Deploy the app to Streamlit Cloud

---

## 🚀 Features

- ✅ Classifies job listings as **REAL** or **FAKE**
- 📝 Input job title and description
- 💻 User-friendly web interface (Streamlit)
- 📊 TF-IDF based feature extraction
- 🧠 Trained on real-world Kaggle dataset

---


---

## 📊 Model Details

- **Text Vectorization**: TF-IDF
- **Model Used**: Logistic Regression
- **Accuracy**: ~95%
- **Training & Testing Split**: 80/20

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas, NumPy
- scikit-learn
- Streamlit
- joblib

---

## ▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/fake-job-posting-detector.git
cd fake-job-posting-detector

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Streamlit app
streamlit run app/app.py


