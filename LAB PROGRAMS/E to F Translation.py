from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Model name
model_name = "Helsinki-NLP/opus-mt-en-fr"

# Load tokenizer and model directly
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# English text
english_text = "Hello, how are you? I am learning NLP."

# Prepare input for the model
inputs = tokenizer(english_text, return_tensors="pt")

# Generate translation
outputs = model.generate(**inputs)

# Decode the output to get the translated text
result = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Display the translation
print("English:", english_text)
print("French:", result)