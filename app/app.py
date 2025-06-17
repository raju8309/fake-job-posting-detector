import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import joblib
from utils.text_cleaning import clean_text

# Load model and vectorizer
model = joblib.load('../models/fake_job_model.pkl')
vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')

# -----------------------
# Streamlit App UI
# -----------------------

st.set_page_config(page_title="Fake Job Detector", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Fake Job Posting Detector")
st.caption("🔍 Enter a job title and description to detect if the posting might be fake.")

# Input fields
title = st.text_input("Job Title")
description = st.text_area("Job Description")

# Button and prediction logic
if st.button("Check if Fake"):
    if title.strip() == "" or description.strip() == "":
        st.warning("⚠️ Please enter both job title and description.")
    else:
        combined = title + " " + description
        cleaned = clean_text(combined)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction == 1:
            st.error("❌ This job looks FAKE!")
        else:
            st.success("✅ This job appears REAL.")
