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
text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""

# Process the example text
result = extract_and_map_entities(text)
print(result)
