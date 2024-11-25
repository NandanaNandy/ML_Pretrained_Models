import spacy
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import json

# Load spaCy lightweight model (en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Load Roberta tokenizer and lightweight model for sequence classification
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
roberta_model = RobertaForSequenceClassification.from_pretrained("roberta-base", return_dict=True)

# Entity Matching and Formatting Function
def process_text(text):
    # Process text using spaCy for NER
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Tokenize text and use Roberta for sequence classification
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = roberta_model(**tokens)
    prediction = outputs.logits.argmax(-1).item()

    # Format the result as JSON
    result = {
        "input_text": text,
        "entities": entities,
        "entity_match_score": prediction
    }
    return json.dumps(result, indent=4)

# Example Usage
text = "Elon Musk founded SpaceX and Tesla in California."
formatted_output = process_text(text)

# Output the JSON
print(formatted_output)
 