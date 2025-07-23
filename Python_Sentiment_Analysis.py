"""
Sentiment Analysis of Political Tweets
---------------------------------------
Simulates pulling tweets from a political figure's Twitter account.
Applies sentiment analysis using TextBlob.

Skills:
- NLP preprocessing
- Sentiment polarity scoring
- DataFrame handling with pandas
- Basic text analytics

Note:
In real projects, Twitter API (via tweepy or snscrape) would be used.
"""

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Simulated tweet data (like from @JoeBiden or any public figure)
data = {
    'date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04'],
    'tweet': [
        "We will rebuild the middle class in America. That's our mission.",
        "Extremist politicians are threatening healthcare access again.",
        "Proud of the bipartisan effort to pass the infrastructure bill.",
        "Gun violence must end. Our kids deserve safe communities."
    ]
}

# Load into DataFrame
df = pd.DataFrame(data)

# Sentiment Analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['polarity'] = df['tweet'].apply(analyze_sentiment)

# Classify sentiment
df['sentiment'] = df['polarity'].apply(
    lambda p: 'Positive' if p > 0 else 'Negative' if p < 0 else 'Neutral'
)

# Print results
print("Sentiment Analysis of Simulated Political Tweets:\n")
print(df[['date', 'tweet', 'sentiment', 'polarity']], "\n")

# Plot
plt.figure(figsize=(8, 5))
df['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.tight_layout()
plt.show()
