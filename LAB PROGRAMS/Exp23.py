
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer
nltk.download('punkt')

# Input text
text = input("Enter a paragraph:\n")

# Step 1: Split paragraph into sentences
sentences = sent_tokenize(text)

# Check whether enough sentences are available
if len(sentences) < 2:
    print("Please enter at least two sentences.")
else:
    # Step 2: Convert sentences into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Step 3: Calculate similarity between consecutive sentences
    similarity_scores = []

    for i in range(len(sentences) - 1):

        score = cosine_similarity(
            tfidf_matrix[i],
            tfidf_matrix[i + 1]
        )[0][0]

        similarity_scores.append(score)

        print("\nSentence", i + 1, ":", sentences[i])
        print("Sentence", i + 2, ":", sentences[i + 1])
        print("Coherence Score:", round(score, 2))

    # Step 4: Calculate average coherence
    average_score = sum(similarity_scores) / len(similarity_scores)

    print("\nAverage Coherence Score:", round(average_score, 2))

    # Step 5: Evaluate coherence
    if average_score >= 0.3:
        print("Result: The text is reasonably coherent.")
    else:
        print("Result: The text has low coherence.")
24.	Create a python program that recognizes dialog acts in a given dialog or conversation.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
sentences = [
    "hello",
    "hi",
    "hey how are you",
    "what is your name",
    "where are you going",
    "how are you",
    "please help me",
    "can you open the door",
    "could you explain this",
    "thank you",
    "thanks for your help",
    "bye",
    "goodbye",
    "see you later",
    "yes I agree",
    "sure I will do it",
    "no I disagree"
]

# Corresponding dialog acts
labels = [
    "Greeting",
    "Greeting",
    "Greeting",
    "Question",
    "Question",
    "Question",
    "Request",
    "Request",
    "Request",
    "Thanks",
    "Thanks",
    "Farewell",
    "Farewell",
    "Farewell",
    "Agreement",
    "Agreement",
    "Disagreement"
]

# Step 1: Convert text into TF-IDF features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(sentences)

# Step 2: Create Naive Bayes model
model = MultinomialNB()

# Step 3: Train the model
model.fit(X, labels)

# Get input from user
text = input("Enter a dialog or conversation:\n")

# Split conversation using comma
utterances = text.split(",")

print("\n--- Dialog Act Recognition ---")

# Predict dialog act for each utterance
for utterance in utterances:

    # Convert input into TF-IDF vector
    input_vector = vectorizer.transform([utterance])

    # Predict dialog act
    prediction = model.predict(input_vector)

    print("\nUtterance:", utterance.strip())
    print("Dialog Act:", prediction[0])
