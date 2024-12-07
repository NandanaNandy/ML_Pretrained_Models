import re
import spacy
import time

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_schema_with_spacy_and_regex(text):
    start_time = time.time()

    # Process the text using spaCy for Named Entity Recognition (NER)
    doc = nlp(text)

    # Define a function to get entities from spaCy output
    def get_entities(label):
        return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

    # Define a function to clean the input text by removing extra spaces and irrelevant characters
    def clean_text(text):
        # Remove unwanted characters and excessive whitespace
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)  # Remove special chars
        cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove extra spaces
        return cleaned_text

    # Function to identify the certificate type based on the content of the text
    def identify_certificate_type(text):
        if 'GATE' in text and 'Score' in text:
            return "gate_score_card"
        elif 'birth' in text and 'certificate' in text:
            return "birth_certificate"
        elif 'degree' in text and 'certificate' in text:
            return "eq_certificate"
        elif 'marksheet' in text and ('10th' in text or '12th' in text):
            return "marksheet_10th" if '10th' in text else "marksheet_12th"
        elif 'disability' in text and 'certificate' in text:
            return "pwd_certificate"
        elif 'experience' in text and 'certificate' in text:
            return "experience_certificate"
        elif 'phd' in text and 'certificate' in text:
            return "phd_certificate"
        else:
            return "unknown"  # Default fallback if no match found

    # Automatically detect the certificate type
    cert_type = identify_certificate_type(text)

    # Define extractors with regex and spaCy entities
    extractors = {
        "gate_score_card": {
            "candidate_name": re.search(r"Name of Candidate[:\s]*([A-Za-z\s]+)", text),
            "parent_name": re.search(r"Parent's/Guardian's Name[:\s]*([A-Za-z\s]+)", text),
            "registration_number": re.search(r"Registration Number[:\s]*([\w-]+)", text),
            "exam_paper": re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text),
            "gate_score": re.search(r"GATE Score[:\s]*([\d.]+)", text),
            "marks": re.search(r"Marks out of 100[:\s]*([\d.]+)", text),
            "rank": re.search(r"All India Rank[:\s]*([\d]+)", text),
            "validity_date": re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text),
            "candidate_name_spacy": get_entities("PERSON"),
            "validity_date_spacy": get_entities("DATE"),
        },
        "birth_certificate": {
            "name": re.search(r"name[:\s]*([\w\s]+)", text),
            "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
            "name_spacy": get_entities("PERSON"),
            "date_of_birth_spacy": get_entities("DATE"),
        },
        "eq_certificate": {
            "name": re.search(r"name[:\s]*([\w\s]+)", text),
            "degree": re.search(r"degree[:\s]*([\w\s]+)", text),
            "cgpa": re.search(r"cgpa[:\s]*([\d.]+)", text),
            "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
            "class": re.search(r"class[:\s]*([\w\s]+)", text),
            "name_spacy": get_entities("PERSON"),
            "degree_spacy": get_entities("ORG"),
        },
        "marksheet_10th": {
            "name": re.search(r"name[:\s]*([\w\s]+)", text),
            "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
            "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
            "board": re.search(r"board[:\s]*([\w\s]+)", text),
            "name_spacy": get_entities("PERSON"),
            "board_spacy": get_entities("ORG"),
        },
        "marksheet_12th": {
            "name": re.search(r"name[:\s]*([\w\s]+)", text),
            "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
            "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
            "board": re.search(r"board[:\s]*([\w\s]+)", text),
            "name_spacy": get_entities("PERSON"),
            "board_spacy": get_entities("ORG"),
        },
        "pwd_certificate": {
            "name": re.search(r"name[:\s]*([\w\s]+)", text),
            "category": re.search(r"category[:\s]*([\w\s]+)", text),
            "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
            "name_spacy": get_entities("PERSON"),
            "category_spacy": get_entities("ORG"),
        }
    }

    # Extract data using regex and spaCy for the specific certificate type
    extracted_data = {}
    for key, value in extractors.get(cert_type, {}).items():
        if isinstance(value, list):  # If the value is a list (from spaCy entities)
            extracted_data[key] = value
        else:  # If the value is a regex match object
            extracted_data[key] = (value.group(1).strip() if value else None)

    # Add the detected certificate type
    extracted_data["certificate_type"] = cert_type

    # Clean up the extracted data fields
    for key in extracted_data:
        if isinstance(extracted_data[key], str):
            extracted_data[key] = clean_text(extracted_data[key])

    # Add processing time
    elapsed_time = time.time() - start_time
    extracted_data["processing_time"] = elapsed_time

    return extracted_data

# Example usage
text = """GATE: GATE 2022 Scorecard Graduate Aptitude Test in Engineering Graduate Aptitude Test in Engineering (GATE) Name of Candidate MOHAMMAD WASIF ANSARI Parent's/Guardian's AKHTARI KHATOON Registration Number 1234567890 Examination Paper Computer Science and Information Technology (CS) GATE Score: 855 Marks out of 100: 63.33 All India Rank in this paper: 68 Valid up to 31st March 2025"""
extracted_data = extract_schema_with_spacy_and_regex(text)
print(extracted_data)
