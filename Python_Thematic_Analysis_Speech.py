"""
Thematic Analysis of Political Speeches
----------------------------------------
Loads a political speech text file, tokenizes it,
filters stopwords, and generates word frequency analysis
with a word cloud.

Skills:
- Text preprocessing with nltk
- Frequency analysis
- Word cloud generation
"""

import nltk
nltk.download('punkt')
nltk.download('stopwords')

import string
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# First-time NLTK setup (uncomment once if needed)
# nltk.download('punkt')
# nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Simulated political speech (replace with file reading if needed)
speech_text = """
My fellow Americans, today we face great challenges but also great opportunities.
We must come together, united in purpose, to rebuild our economy,
protect our freedoms, and secure a better future for all.
"""

# --- Text Preprocessing ---
tokens = word_tokenize(speech_text.lower())
words = [word for word in tokens if word.isalpha()]
filtered_words = [word for word in words if word not in stopwords.words('english')]

# --- Frequency Analysis ---
word_freq = Counter(filtered_words)

# Print most common words
print("Top 10 Frequent Words:\n")
for word, freq in word_freq.most_common(10):
    print(f"{word}: {freq}")

# --- Word Cloud Visualization ---
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Thematic Word Cloud of Political Speech")
plt.tight_layout()
plt.show()
