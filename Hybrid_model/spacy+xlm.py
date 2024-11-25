import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import time

# Load spaCy's English model
nlp_spacy = spacy.load("en_core_web_sm")

# Load Hugging Face's multilingual NER pipeline using xlm-roberta
tokenizer = AutoTokenizer.from_pretrained("Davlan/xlm-roberta-base-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained("Davlan/xlm-roberta-base-ner-hrl")
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Function to extract entities using spaCy for English text
def extract_entities_spacy(text):
    """
    Extract entities using spaCy's NER model.
    Args:
        text (str): Input text in English.
    Returns:
        list: Extracted entities with labels.
    """
    doc = nlp_spacy(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

# Function to extract entities using xlm-roberta for multilingual text
def extract_entities_xlmroberta(text):
    """
    Extract entities using xlm-roberta NER model.
    Args:
        text (str): Input text in any language.
    Returns:
        list: Extracted entities with labels.
    """
    results = ner_pipeline(text)
    return [{"text": ent["word"], "label": ent["entity_group"]} for ent in results]

# Unified processing function
def process_text(input_text, language="english"):
    """
    Process the input text to extract entities and measure execution time.
    Args:
        input_text (str): The text to process.
        language (str): Language of the text ('english' or 'multilingual').
    Returns:
        tuple: Extracted entities and execution time.
    """
    print(f"Processing text ({language}): {input_text[:100]}...")  # Show a preview of the input text

    start_time = time.time()
    if language.lower() == "english":
        entities = extract_entities_spacy(input_text)
    else:
        entities = extract_entities_xlmroberta(input_text)
    execution_time = time.time() - start_time

    return entities, execution_time

# Example: Input texts in different languages
input_texts = [
    # English text
    ("This is to certify that Selvan Nareshkanna, son of Thiru Shanmugam, residing at Door No. 164/5, Periyar Nagar, "
     "of Harur Village / Town Harur Taluk Dharmapuri District of the State of Tamil Nadu belongs to 24 Manai Telugu "
     "Chetty Community, which is recognized as a Backward Class as per Government Order (Ms.) No. 85, Backward Classes, "
     "Most Backward Classes and Minority Welfare Department (BCC), dated 29th July 2008.", "english"),

    # Tamil text
    ("இது பெரியார் நகர் கதவு எண் 164/5ல் வசிக்கும் திரு சண்முகத்தின் மகன் செல்வன் நரேஷ்கண்ணா என்று சான்றளிக்கத்தான். "
     "தமிழ்நாடு மாநிலத்தின் ஹரூர் தாலுகா தர்மபுரி மாவட்டம் ஹரூர் கிராமம் / டவுன் 24 மனை தெலுங்குக்கு சொந்தமானது "
     "அரசு ஆணை (செல்வி) எண். 85ன் படி பிற்படுத்தப்பட்ட வகுப்பாக அங்கீகரிக்கப்பட்ட செட்டி சமூகம், பிற்படுத்தப்பட்ட வகுப்பினர், "
     "மிகவும் பிற்படுத்தப்பட்டோர் மற்றும் சிறுபான்மையினர் நலத் துறை (பிசிசி), தேதி 29 ஜூலை 2008.", "multilingual"),
    
    # Hindi text
    ("यह प्रमाणित किया जाता है कि सेल्वन नरेशकन्ना, थिरु शनमुगम के पुत्र, डोर नंबर 164/5, पेरियार नगर में रहते हैं।"
     "तमिलनाडु राज्य के हरूर गांव/नगर हरूर तालुक धर्मपुरी जिले का 24 मनई तेलुगु क्षेत्र है"
     "चेट्टी समुदाय, जिसे सरकारी आदेश (सुश्री) संख्या 85, पिछड़ा वर्ग के अनुसार पिछड़ा वर्ग के रूप में मान्यता प्राप्त है,"
     "अति पिछड़ा वर्ग एवं अल्पसंख्यक कल्याण विभाग (बीसीसी), दिनांक 29 जुलाई 2008।", "अंग्रेजी")
]

# Process and display results for each input text
for idx, (text, lang) in enumerate(input_texts):
    print(f"\n--- Example {idx + 1} ---")
    entities, execution_time = process_text(text, language=lang)
    print("Extracted Entities:")
    for entity in entities:
        print(f"Entity: {entity['text']}, Label: {entity['label']}")
    print(f"Execution Time: {execution_time:.4f} seconds")
def calculate_metrics(predicted_entities, ground_truth_entities):
    """
    Calculate precision, recall, F1 score, and accuracy for NER predictions.

    Args:
        predicted_entities (list): List of dictionaries with 'text' and 'label' for predictions.
        ground_truth_entities (list): List of dictionaries with 'text' and 'label' for ground truth.

    Returns:
        dict: Dictionary with precision, recall, F1 score, and accuracy.
    """
    # Convert to sets for easier comparison
    predicted_set = {(ent['text'], ent['label']) for ent in predicted_entities}
    ground_truth_set = {(ent['text'], ent['label']) for ent in ground_truth_entities}

    # Calculate metrics
    true_positives = len(predicted_set & ground_truth_set)
    false_positives = len(predicted_set - ground_truth_set)
    false_negatives = len(ground_truth_set - predicted_set)

    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    accuracy = true_positives / len(ground_truth_set) if len(ground_truth_set) > 0 else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
        "accuracy": accuracy
    }

# Example Ground Truth for English text
ground_truth_entities_english = [
    {"text": "Selvan Nareshkanna", "label": "PERSON"},
    {"text": "Thiru Shanmugam", "label": "PERSON"},
    {"text": "Door No. 164/5", "label": "ADDRESS"},
    {"text": "Periyar Nagar", "label": "ADDRESS"},
    {"text": "Harur", "label": "LOCATION"},
    {"text": "Dharmapuri District", "label": "LOCATION"},
    {"text": "Tamil Nadu", "label": "LOCATION"},
    {"text": "24 Manai Telugu Chetty Community", "label": "ORGANIZATION"},
    {"text": "Backward Class", "label": "CATEGORY"},
    {"text": "29th July 2008", "label": "DATE"}
]

# Process English text
predicted_entities, _ = process_text(input_texts[0][0], language="english")

# Calculate metrics
metrics = calculate_metrics(predicted_entities, ground_truth_entities_english)

print("\nMetrics for English Text:")
for metric, value in metrics.items():
    print(f"{metric.capitalize()}: {value:.4f}")
