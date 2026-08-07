import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Input text
text = input("Enter a sentence: ")

# Tokenization
words = word_tokenize(text)

# Create stemmer
stemmer = PorterStemmer()

print("\nMorphological Analysis:")

for word in words:
    root_word = stemmer.stem(word)
    print(word, "-->", root_word)