from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive 😊"
    elif sentiment < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    print("Enter a text to analyze its sentiment:")
    user_input = input("> ")
    result = analyze_sentiment(user_input)
    print(f"Sentiment: {result}")
