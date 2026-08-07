# Transformation based tagging

words = ["I", "book", "a", "book"]

# Initial tagging
tags = ["NOUN"] * len(words)

# Transformation rule:
# If word is "I", change tag to PRON

for i in range(len(words)):
    if words[i] == "I":
        tags[i] = "PRON"

print("Word\tTag")
print("----------------")

for word, tag in zip(words, tags):
    print(word, "\t", tag)