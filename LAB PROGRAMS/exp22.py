import re

text = "John went to the library. He borrowed a book."

# Split text into sentences
sentences = re.split(r'[.!?]', text)

# Store previously mentioned nouns
entities = []

pronouns = ["he", "she", "it", "they", "him", "her", "them"]

for sentence in sentences:
    words = sentence.strip().split()

    for word in words:
        clean_word = word.lower().strip(",.")

        # Detect pronouns
        if clean_word in pronouns:
            if entities:
                print(f"{word} refers to {entities[-1]}")

        # Detect simple proper nouns
        elif word[0].isupper():
            entities.append(word.strip(",."))
