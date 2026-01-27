from nltk.corpus import stopwords
from nltk.tokenize import work_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer

text = """The product quality is very good and I am extremely happy with the service.
            The delivery was late, but the customer supportes was helpful.
            Overall, the experience was positive and I would recommended this company."""

words=[w for w in word.tokenize(text.lower()) if w.usalpha() and w not in stopwords.words('english')]
print("Words after Stop words removal\n", words)

porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
regex = RegexpStemmer('ing$|ed$|ly$|s$|es$')
print("\nPorter Stemmer :", [porter.stem(w) for w in words])
print("\nSnowball Stemmer :",[snowball.stem(w) for w in words])
print("\nLancaster Stemmer:",[lancaster.stem(w) for w in words])
print("\nRegexp Stemmer:",[regex.stem(w) for w in words])
