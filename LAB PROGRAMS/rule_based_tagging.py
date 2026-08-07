#rule based tagging
import re

words = input("Enter sentence: ").split()

print("\nWord\tPOS Tag")
print("----------------")

for word in words:

    if re.match(r'.*ing$', word):
        tag = "VERB"

    elif re.match(r'.*ly$', word):
        tag = "ADV"

    elif re.match(r'.*ous$', word):
        tag = "ADJ"

    elif re.match(r'.*s$', word):
        tag = "NOUN"

    else:
        tag = "NOUN"

    print(word, "\t", tag)