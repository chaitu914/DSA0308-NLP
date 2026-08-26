# Simple Top-Down Parser for CFG

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["ball"]],
    "V": [["eats"], ["kicks"]]
}


# Check whether a symbol is a non-terminal
def is_non_terminal(symbol):
    return symbol in grammar


# Top-down parsing function
def parse(symbol, words, position):

    # If symbol is a terminal
    if not is_non_terminal(symbol):

        if position < len(words) and symbol == words[position]:
            return position + 1

        return -1

    # Try each grammar rule
    for rule in grammar[symbol]:

        current_position = position
        success = True

        for item in rule:

            current_position = parse(
                item, words, current_position
            )

            if current_position == -1:
                success = False
                break

        if success:
            return current_position

    return -1


# Main program
sentence = input("Enter sentence: ").lower().split()

result = parse("S", sentence, 0)

if result == len(sentence):
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")