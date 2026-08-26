import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define Probabilistic Context-Free Grammar
grammar = PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Det N [0.5]
NP -> Det Adj N [0.3]
NP -> 'John' [0.2]

VP -> V NP [0.6]
VP -> V [0.4]

Det -> 'the' [0.6]
Det -> 'a' [0.4]

Adj -> 'big' [0.5]
Adj -> 'small' [0.5]

N -> 'dog' [0.5]
N -> 'cat' [0.5]

V -> 'sees' [0.5]
V -> 'runs' [0.5]
""")

# Create Viterbi Parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "the big dog sees a cat".split()

print("Sentence:", " ".join(sentence))
print("\nParse Tree:")

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
    print("\nProbability:", tree.prob())