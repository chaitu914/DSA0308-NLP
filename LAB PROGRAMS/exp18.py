import re

def parse_fopc(expression):
    print("Expression:", expression)

    # Find quantifiers
    quantifiers = re.findall(r'\b(forall|exists)\b', expression)

    # Find predicates
    predicates = re.findall(r'([A-Z][A-Za-z0-9_]*)\s*\((.*?)\)', expression)

    # Find logical operators
    operators = re.findall(r'(AND|OR|NOT|IMPLIES)', expression)

    # Find variables and constants inside predicates
    terms = []
    for predicate, arguments in predicates:
        args = [x.strip() for x in arguments.split(',')]
        terms.append((predicate, args))

    print("Quantifiers:", quantifiers)
    print("Predicates:", terms)
    print("Operators:", operators)

# Example
expression = "forall x Human(x) IMPLIES Mortal(x)"

parse_fopc(expression)