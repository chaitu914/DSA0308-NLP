def recognize_dialog_act(sentence):
    text = sentence.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "good morning"]):
        return "Greeting"

    elif "?" in sentence:
        return "Question"

    elif any(word in text for word in ["please", "can you", "could you"]):
        return "Request"

    elif any(word in text for word in ["thank you", "thanks"]):
        return "Thanking"

    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye"

    elif any(word in text for word in ["yes", "no", "okay", "sure"]):
        return "Answer/Confirmation"

    else:
        return "Statement"


sentence = input("Enter a dialog: ")

dialog_act = recognize_dialog_act(sentence)

print("Dialog Act:", dialog_act)