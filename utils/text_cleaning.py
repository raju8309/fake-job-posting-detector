# utils/text_cleaning.py

import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Cleans text by removing URLs, HTML, punctuation, and stopwords.
    """
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", '', text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

