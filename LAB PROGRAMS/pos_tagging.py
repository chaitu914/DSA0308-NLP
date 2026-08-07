import nltk
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

text = "The boys are playing in the ground."

# Tokenization
words = word_tokenize(text)

# POS Tagging
tags = nltk.pos_tag(words)

# Print results
for word, tag in tags:
    print(word, tag)