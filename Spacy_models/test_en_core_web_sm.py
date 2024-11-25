import re
import spacy
import time

nlp = spacy.load("en_core_web_sm")

def extract_key_value_pairs(text):
    entities = {}

    doc = nlp(text)

    key_value_patterns = {
        "certificate_no": r"Certificate No[:\s]*([\w\-\/]+)",
        "registration_no": r"Registration No[:\s]*([\w\-\/]+)",  
        "name": r"that\s([A-Za-z\s]+),", 
        "father_name": r"son of\s([A-Za-z\s]+) and", 
        "mother_name": r"mother\s([A-Za-z\s]+),",  
        "address": r"residing at\s([\d\w\s,\/\-]+),",  
        "community": r"belongs to\s([\d\w\s]+(?:Community)*)", 
        "date_of_birth": r"(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4})", 
        "phone": r"Phone[:\s]*([\+\(\)\d\s\-]+)", 
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  
        "district": r"District[:\s]*([A-Za-z]+)", 
        "taluk": r"Taluk[:\s]*([A-Za-z]+)", 
        "mark": r"Mark\s([\w\s]+(?:Mark)*)",  
        "caste": r"caste\s([\w\s]+(?:caste)*)",  
    }

    for key, pattern in key_value_patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            entities[key] = [match.strip() for match in matches]

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if "person" not in entities:
                entities["person"] = [ent.text]
            else:
                entities["person"].append(ent.text)
        elif ent.label_ == "GPE" or ent.label_ == "LOC":
            if "location" not in entities:
                entities["location"] = [ent.text]
            else:
                entities["location"].append(ent.text)
        elif ent.label_ == "DATE":
            if "date" not in entities:
                entities["date"] = [ent.text]
            else:
                entities["date"].append(ent.text)

    return entities


text = """
This is to certify that Mr. James A. Smith, born on 14th May 1985, residing at 1234 Elm Street, Springfield, Illinois, USA, 
has been issued this document with Certificate No: RH-987654321 and Registration No: BIRTH/2024/00123. The individual’s roll number for 
academic purposes is 12345. The birth took place at Springfield General Hospital, Springfield, and the certificate was issued at Springfield Municipality Office. 
This certificate confirms that the individual qualifies under a healthcare plan with a recorded disability of 40%. The declared annual income of the family is 3,00,000. 
For further inquiries, contact Phone: +1 (555) 123-4567 or Email: james.smith@example.com. The individual belongs to the community of General Category.
"""

start_time = time.time()

extracted_entities = extract_key_value_pairs(text)

print("Extracted Entities:")
for key, values in extracted_entities.items():
    print(f"{key}: {', '.join(values)}")

end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.2f} seconds")