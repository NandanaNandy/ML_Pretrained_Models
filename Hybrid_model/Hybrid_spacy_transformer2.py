import spacy
from spacy.matcher import Matcher
import re
from datetime import datetime

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Define matcher patterns for rule-based extraction
matcher.add("CERTIFICATE_NO", [[{"LOWER": "certificate"}, {"LOWER": "no."}, {"IS_ASCII": True, "LENGTH": 19}]])
matcher.add("NAME", [[{"LOWER": "certify"}, {"IS_TITLE": True, "OP": "+"}, {"LOWER": "son"}, {"LOWER": "of"}]])
matcher.add("FATHER_NAME", [[{"LOWER": "son"}, {"LOWER": "of"}, {"IS_TITLE": True, "OP": "+"}]])
matcher.add("GENDER", [[{"LOWER": "male"}, {"IS_ALPHA": False, "OP": "?"}]])
matcher.add("ADDRESS", [[{"LOWER": "resident"}, {"LOWER": "of"}, {"IS_ALPHA": True, "OP": "+"}]])
matcher.add("SUB_DISTRICT", [[{"LOWER": "sub"}, {"LOWER": "district"}, {"LOWER": ":"}, {"IS_ALPHA": True, "OP": "+"}]])
matcher.add("DISTRICT", [[{"LOWER": "district"}, {"LOWER": ":"}, {"IS_ALPHA": True, "OP": "+"}]])
matcher.add("STATE_UT", [[{"LOWER": "state"}, {"LOWER": "/"}, {"LOWER": "ut"}, {"LOWER": "delhi"}]])

# Regex patterns for structured fields
regex_patterns = {
    "certificate_no": r"Certificate No\.: ([A-Z0-9]+)",
    "date": r"Date:\s([\d/]+)",
    "date_of_birth": r"Date of Birth ([\d/]+)",
    "age": r"Age (\d+)",
    "registration_no": r"Registration No\.\s([\d/]+)",
    "disability_type": r"He is a case of ([\w\s]+)",
    "diagnosis": r"The diagnosis in his case is ([\w\s]+)",
    "disability_percentage": r"He has (\d+)% \(in figure\)",
    "valid_until": r"shall be valid till ([\d/]+)",
    "document_type": r"Nature of Document\(s\): ([\w\s]+)",
    "medical_authority_name": r"Signature / Thumb Impression[\s\S]+by ([\w\s]+)",
    "medical_authority_reg_no": r"Regn\. No\.([\w\s()-]+)",
    "designation": r"Designation: ([\w\s]+)",
    "institution_name": r"Department of ([\w\s]+)",
    "institution_address": r"institution address ([\w\s,]+)"
}

# Function to apply spaCy matcher
def extract_entities(text):
    doc = nlp(text)
    matches = matcher(doc)
    entities = {}
    for match_id, start, end in matches:
        span = doc[start:end]
        label = nlp.vocab.strings[match_id]
        entities[label] = span.text
    return entities

# Function to extract fields using regex
def extract_with_regex(patterns, text):
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        extracted[key] = match.group(1).strip() if match else None
    return extracted

# Main function to extract data dynamically
def extract_dynamic_schema(input_text):
    # Extract entities with spaCy
    entities = extract_entities(input_text)

    # Extract fields with regex
    regex_extracted = extract_with_regex(regex_patterns, input_text)

    # Parse fields
    output = {
        "certificate_no": regex_extracted.get("certificate_no", entities.get("CERTIFICATE_NO", "")),
        "date": regex_extracted.get("date", ""),
        "name": regex_extracted.get("name", entities.get("NAME", "")).replace("certify ", ""),
        "father_name": regex_extracted.get("father_name", entities.get("FATHER_NAME", "")).replace("son of ", ""),
        "date_of_birth": regex_extracted.get("date_of_birth", ""),
        "age": int(regex_extracted.get("age", 0)),
        "gender": regex_extracted.get("gender", entities.get("GENDER", "")),
        "registration_no": regex_extracted.get("registration_no", ""),
        "address": regex_extracted.get("address", entities.get("ADDRESS", "")).replace("resident of ", ""),
        "sub_district": regex_extracted.get("sub_district", entities.get("SUB_DISTRICT", "").replace("sub district: ", "")),
        "district": regex_extracted.get("district", entities.get("DISTRICT", "").replace("district: ", "")),
        "state_ut": regex_extracted.get("state_ut", entities.get("STATE_UT", "").replace("state / ut ", "")),
        "disability_type": regex_extracted.get("disability_type", ""),
        "diagnosis": regex_extracted.get("diagnosis", ""),
        "disability_percentage": int(regex_extracted.get("disability_percentage", 0)),
        "valid_until": regex_extracted.get("valid_until", ""),
        "document_type": regex_extracted.get("document_type", ""),
        "medical_authority_name": regex_extracted.get("medical_authority_name", ""),
        "medical_authority_reg_no": regex_extracted.get("medical_authority_reg_no", ""),
        "designation": regex_extracted.get("designation", ""),
        "institution_name": regex_extracted.get("institution_name", ""),
        "institution_address": regex_extracted.get("institution_address", "")
    }

    return output

# Sample input
input_text = """
सत्यमेव जमी
Department of Empowerment of Persons with Disabilities, Ministry of Social Justice and Empowerment, Government of India
Disability Certificate Issuing Medical Authority, Shahdara, Delhi
Certificate No.: DL0820920060023881
Date: 03/05/2023
This is to certify that I/we have carefully examined Shri Krishna Agarwal, Son of Shri Yogesh Kumar, Date of Birth 08/07/2006, Age 16, Male, Registration No. 0708/00000/2212/0734922, resident of House No. 1/11110, Street No-9, Near Kirti Mandir, West Subhash Park, Shahdara, East Delhi, Delhi 110032, Sub District Shahdara, District Shahdara, State / UT Delhi, whose photograph is affixed above, and I am/we are satisfied that:
(A) He is a case of Intellectual Disability
(B) The diagnosis in his case is Severe Intellectual Impairment
(C) He has 90% (in figure) Ninety percent(in words) Temporary Disability in relation to his Brain as per the guidelines (Guidelines for the purpose of assessing the extent of specified disability in a person included under RPWD Act, 2016 notified by Government of India vide S.O. 76(E) dated 04/01/2018).
This certificate recommended for 1 year(s) 2 month(s), and therefore this certificate shall be valid till 03/07/2024
The applicant has submitted the following document(s) as proof of residence:
Nature of Document(s): Aadhaar card
Signature / Thumb Impression of the Person with Disability
Dr. UDAY KUMAR SINHA
Regn. No.A-000826 (RC) Additional Professor
Department of Clinical Psychology Dr. Anggawat HBAS, Delhi-110095
"""

# Extract schema dynamically
output_schema = extract_dynamic_schema(input_text)
print(output_schema)
