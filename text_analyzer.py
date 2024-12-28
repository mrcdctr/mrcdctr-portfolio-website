import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_text(text):
    words = len(text.split())
    chars = len(text)
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    print(f"Word Count: {words}")
    print(f"Character Count: {chars}")
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    sample_text = input("Enter a text to analyze: ")
    analyze_text(sample_text)
