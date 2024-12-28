import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.data import find

# Check and download 'vader_lexicon' if not present
try:
    find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

@st.cache_resource
def get_sentiment_analyzer():
    return SentimentIntensityAnalyzer()

def analyze_text(text, sia):
    words = len(text.split())
    chars = len(text)
    sentiment = sia.polarity_scores(text)
    return words, chars, sentiment

# Streamlit UI
st.title("Text Analyzer Web App")
st.subheader("Analyze word count, character count, and sentiment")

# Text input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    trimmed_input = user_input.strip()
    if trimmed_input:
        sia = get_sentiment_analyzer()
        words, chars, sentiment = analyze_text(trimmed_input, sia)
        st.write(f"**Word Count:** {words}")
        st.write(f"**Character Count:** {chars}")
        st.write("**Sentiment Analysis:**")
        st.json(sentiment)
    else:
        st.warning("Please enter some valid text to analyze.")

