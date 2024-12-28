import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_text(text):
    words = len(text.split())
    chars = len(text)
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    return words, chars, sentiment

# Streamlit UI
st.title("Text Analyzer Web App")
st.subheader("Analyze word count, character count, and sentiment")

# Text input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input:
        words, chars, sentiment = analyze_text(user_input)
        st.write(f"**Word Count:** {words}")
        st.write(f"**Character Count:** {chars}")
        st.write("**Sentiment Analysis:**")
        st.json(sentiment)
    else:
        st.warning("Please enter some text to analyze.")
