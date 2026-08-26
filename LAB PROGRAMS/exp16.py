import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = """
Sundar Pichai is the CEO of Google.
Google is headquartered in Mountain View, California.
He was born in Chennai, India.
"""

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities:")
print("----------------")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)