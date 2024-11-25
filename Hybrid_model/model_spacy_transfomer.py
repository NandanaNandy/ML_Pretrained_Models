import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from torch.nn.functional import softmax
import json

# Load spaCy transformer-based model
nlp_spacy = spacy.load("en_core_web_trf")

# Load Hugging Face Transformer model
ner_model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
ner_tokenizer = AutoTokenizer.from_pretrained(ner_model_name)
ner_model = AutoModelForTokenClassification.from_pretrained(ner_model_name)

# Define function to extract entities using Hugging Face
def extract_entities_hf(text):
    tokens = ner_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = ner_model(**tokens).logits
    predictions = torch.argmax(outputs, dim=-1).squeeze().tolist()
    tokens_decoded = ner_tokenizer.convert_ids_to_tokens(tokens["input_ids"].squeeze())
    labels = ner_model.config.id2label
    entities = []
    for token, pred in zip(tokens_decoded, predictions):
        label = labels.get(pred, "O")
        if label != "O":  # Filter only named entities
            entities.append({"text": token, "label": label})
    return entities

# Define function to combine spaCy and Hugging Face outputs
def extract_and_map_entities(text):
    # Process with spaCy
    doc = nlp_spacy(text)
    spacy_entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    relationships = [{"token": tok.text, "dep": tok.dep_, "head": tok.head.text} for tok in doc]

    # Extract entities using Hugging Face
    hf_entities = extract_entities_hf(text)

    # Combine results
    combined_entities = {
        "spacy_entities": spacy_entities,
        "hf_entities": hf_entities,
        "relationships": relationships
    }
    return json.dumps(combined_entities, indent=4)

# Example text
example_text = """
Dr. A.P.J. Abdul Kalam, born on 15 October 1931, was a scientist in DRDO and ISRO. 
He completed his studies at MIT, Chennai, and later served as the 11th President of India.
"""

# Process the example text
result = extract_and_map_entities(example_text)
print(result)
