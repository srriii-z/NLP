import os

import re
from collections import Counter
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from textblob import TextBlob

posts = [
    "i love this new phone battery life is amazing",
    "This update is very bad and disappointing",
    "Amazing camera and great performance",
    "The app is slow and the interface is bad",
    "i love the camera qulaity and battery performance"
]

stwords = set(stopwords.words('english'))
ug, bg, tg = [], [], []

for post in posts:
    post = post.lower()
    post = re.sub(r'[^a-z\s]', '', post)
    words = [w for w in post.split() if w not in stwords]
    
    ug.extend(words)
    bg.extend(zip(words, words[1:]))
    tg.extend(zip(words, words[1:], words[2:]))

ugc = Counter(ug)
bgc = Counter(bg)
tgc = Counter(tg)

print("Top Unigrams:", ugc.most_common(3))
print("\nTop Bigrams:", bgc.most_common(3))
print("\nTop Trigrams:", tgc.most_common(3))

print("\nSentiment Analysis")

for post in posts:
    blob = TextBlob(post)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"Post: '{post}'")
    print(f"Sentiment: {sentiment}, Polarity: {polarity}\n")
