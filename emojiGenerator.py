from textblob import TextBlob
import emoji

# Function to map sentiment to emoji
def get_emoji(sentiment):
    if sentiment > 0.5:
        return emoji.emojize("😄", language='alias')
    elif sentiment > 0.1:
        return emoji.emojize("🙂", language='alias')
    elif sentiment < -0.5:
        return emoji.emojize("😠", language='alias')
    elif sentiment < -0.1:
        return emoji.emojize("☹️", language='alias')
    else:
        return emoji.emojize("😐", language='alias')

# Ask user to enter a sentence
text = input("Enter a sentence: ")

# Analyze the sentiment
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity

# Get the emoji
output_emoji = get_emoji(sentiment_score)

# Show result
print(f"\nSentiment score: {sentiment_score}")
print(f"Suggested emoji: {output_emoji}")