import re
import spacy
import time
import torch

# Check if CUDA is available for PyTorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Ensure SpaCy is using GPU if available
try:
    spacy.require_gpu()  # This will raise an error if GPU is not available
    print("SpaCy will use GPU.")
except:
    print("SpaCy will use CPU. Ensure that CUDA is properly installed and configured.")

# Load SpaCy model with GPU support if available
nlp = spacy.load("en_core_web_sm")

def extract_key_value_pairs(text):
    entities = {}

    key_value_patterns = {
        "certificate_no": r"Certificate No[:\s]*([\w\-\/]+)", 
        "registration_no": r"Registration No[:\s]*([\w\-\/]+)", 
        "name": r"that\s+(Mr\.|Ms\.|Mrs\.|Dr\.)\s+([A-Za-z]+(?:\s+[A-Za-z]+)*)", 
        "address": r"residing at\s+([\w\s,\/\-]+?)(?=,?\s+(has been|and the|with Certificate|$))",  
        "community": r"belongs to\s+([\w\s]+(?:Community|Category))",  
        "date_of_birth": r"\b(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4})\b", 
        "phone": r"Phone[:\s]*([\+\(\)\d\s\-]+)",  
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", 
        "location": r"at\s+([\w\s]+(?:Municipality|Hospital|Office))",  
    }

    for key, pattern in key_value_patterns.items():
        match = re.search(pattern, text)
        if match:
            if key == "name" and len(match.groups()) >= 2:
                entities[key] = f"{match.group(1)} {match.group(2)}".strip()
            elif len(match.groups()) >= 1:
                entities[key] = match.group(1).strip()

    doc = nlp(text)
    if "name" not in entities: 
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["name"] = ent.text
                break  

    return entities

def process_text(input_text):
    start_time = time.time()

    extracted_entities = extract_key_value_pairs(input_text)

    print("Extracted Entities:")
    for key, value in extracted_entities.items():
        print(f"{key}: {value}")

    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.2f} seconds")

sample_input_text = """
This is to certify that Mr. James A. Smith, born on 14th May 1985, residing at 1234 Elm Street, Springfield, Illinois, USA, 
has been issued this document with Certificate No: RH-987654321 and Registration No: BIRTH/2024/00123. The individual’s roll number for 
academic purposes is 12345. The birth took place at Springfield General Hospital, Springfield, and the certificate was issued at Springfield Municipality Office. 
This certificate confirms that the individual qualifies under a healthcare plan with a recorded disability of 40%. The declared annual income of the family is 3,00,000. 
For further inquiries, contact Phone: +1 (555) 123-4567 or Email: james.smith@example.com. The individual belongs to the community of General Category.
"""

process_text(sample_input_text)
