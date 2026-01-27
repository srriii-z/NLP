import nltk
nltk.download('punkt_tab')
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer
text = """the product quality is very good and i am extremely happy with the service.
the delivery was late, but the customer support was helpful.
overall, the experience was positive and i would recommend this company."""
words = [
    w for w in word_tokenize(text.lower())
    if w.isalpha() and w not in stopwords.words('english')]

print("Words after stop words removal:\n", words)
porter = PorterStemmer()
sb = SnowballStemmer("english")
lc = LancasterStemmer()
regex = RegexpStemmer('ing$|ed$|ly$|s$|es$')
print("\nPorter Stemmer")
print([porter.stem(w) for w in words])
print("\nSnowball Stemmer")
print([sb.stem(w) for w in words])
print("\nLancaster Stemmer")
print([lc.stem(w) for w in words])
print("\nRegex Stemmer")
print([regex.stem(w) for w in words])
