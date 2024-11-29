from transformers import pipeline
nlp = pipeline("ner", model="ai4bharat/IndicNER")
text = "அவரின் பெயர் ஜான் டோ, பிறந்த தேதி 5 மார்ச் 1990."
entities = nlp(text)
for entity in entities:
    print(f"{entity['entity']} -> {entity['word']}")
