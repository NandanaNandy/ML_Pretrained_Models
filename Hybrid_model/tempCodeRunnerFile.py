# import spacy
# from spacy.matcher import Matcher
# import re
# from datetime import datetime

# # Load spaCy NLP model
# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)

# # Define matcher patterns for rule-based extraction
# matcher.add("CERTIFICATE_NO", [[{"LOWER": "certificate"}, {"LOWER": "no."}, {"IS_ASCII": True, "LENGTH": 19}]])
# matcher.add("NAME", [[{"LOWER": "certify"}, {"IS_TITLE": True, "OP": "+"}, {"LOWER": "son"}, {"LOWER": "of"}]])
# matcher.add("FATHER_NAME", [[{"LOWER": "son"}, {"LOWER": "of"}, {"IS_TITLE": True, "OP": "+"}]])
# matcher.add("GENDER", [[{"LOWER": "male"}, {"IS_ALPHA": False, "OP": "?"}]])
# matcher.add("ADDRESS", [[{"LOWER": "resident"}, {"LOWER": "of"}, {"IS_ALPHA": True, "OP": "+"}]])
# matcher.add("SUB_DISTRICT", [[{"LOWER": "sub"}, {"LOWER": "district"}, {"LOWER": ":"}, {"IS_ALPHA": True, "OP": "+"}]])
# matcher.add("DISTRICT", [[{"LOWER": "district"}, {"LOWER": ":"}, {"IS_ALPHA": True, "OP": "+"}]])
# matcher.add("STATE_UT", [[{"LOWER": "state"}, {"LOWER": "/"}, {"LOWER": "ut"}, {"LOWER": "delhi"}]])

# # Regex patterns for structured fields
# regex_patterns = {
#     "certificate_no": r"Certificate No\.: ([A-Z0-9]+)",
#     "date": r"Date:\s([\d/]+)",
#     "date_of_birth": r"Date of Birth ([\d/]+)",
#     "age": r"Age (\d+)",
#     "registration_no": r"Registration No\.\s([\d/]+)",
#     "disability_type": r"He is a case of ([\w\s]+)",
#     "diagnosis": r"The diagnosis in his case is ([\w\s]+)",
#     "disability_percentage": r"He has (\d+)% \(in figure\)",
#     "valid_until": r"shall be valid till ([\d/]+)",
#     "document_type": r"Nature of Document\(s\): ([\w\s]+)",
#     "medical_authority_name": r"Signature / Thumb Impression[\s\S]+by ([\w\s]+)",
#     "medical_authority_reg_no": r"Regn\. No\.([\w\s()-]+)",
#     "designation": r"Designation: ([\w\s]+)",
#     "institution_name": r"Department of ([\w\s]+)",
#     "institution_address": r"institution address ([\w\s,]+)"
# }

# # Function to apply spaCy matcher
# def extract_entities(text):
#     doc = nlp(text)
#     matches = matcher(doc)
#     entities = {}
#     for match_id, start, end in matches:
#         span = doc[start:end]
#         label = nlp.vocab.strings[match_id]
#         entities[label] = span.text
#     return entities

# # Function to extract fields using regex
# def extract_with_regex(patterns, text):
#     extracted = {}
#     for key, pattern in patterns.items():
#         match = re.search(pattern, text)
#         extracted[key] = match.group(1).strip() if match else None
#     return extracted

# # Main function to extract data dynamically
# def extract_dynamic_schema(input_text):
#     # Extract entities with spaCy
#     entities = extract_entities(input_text)

#     # Extract fields with regex
#     regex_extracted = extract_with_regex(regex_patterns, input_text)

#     # Parse fields
#     output = {
#         "certificate_no": regex_extracted.get("certificate_no", entities.get("CERTIFICATE_NO", "")),
#         "date": regex_extracted.get("date", ""),
#         "name": regex_extracted.get("name", entities.get("NAME", "")).replace("certify ", ""),
#         "father_name": regex_extracted.get("father_name", entities.get("FATHER_NAME", "")).replace("son of ", ""),
#         "date_of_birth": regex_extracted.get("date_of_birth", ""),
#         "age": int(regex_extracted.get("age", 0)),
#         "gender": regex_extracted.get("gender", entities.get("GENDER", "")),
#         "registration_no": regex_extracted.get("registration_no", ""),
#         "address": regex_extracted.get("address", entities.get("ADDRESS", "")).replace("resident of ", ""),
#         "sub_district": regex_extracted.get("sub_district", entities.get("SUB_DISTRICT", "").replace("sub district: ", "")),
#         "district": regex_extracted.get("district", entities.get("DISTRICT", "").replace("district: ", "")),
#         "state_ut": regex_extracted.get("state_ut", entities.get("STATE_UT", "").replace("state / ut ", "")),
#         "disability_type": regex_extracted.get("disability_type", ""),
#         "diagnosis": regex_extracted.get("diagnosis", ""),
#         "disability_percentage": int(regex_extracted.get("disability_percentage", 0)),
#         "valid_until": regex_extracted.get("valid_until", ""),
#         "document_type": regex_extracted.get("document_type", ""),
#         "medical_authority_name": regex_extracted.get("medical_authority_name", ""),
#         "medical_authority_reg_no": regex_extracted.get("medical_authority_reg_no", ""),
#         "designation": regex_extracted.get("designation", ""),
#         "institution_name": regex_extracted.get("institution_name", ""),
#         "institution_address": regex_extracted.get("institution_address", "")
#     }

#     return output

# # Sample input
# input_text = """
# सत्यमेव जमी
# Department of Empowerment of Persons with Disabilities, Ministry of Social Justice and Empowerment, Government of India
# Disability Certificate Issuing Medical Authority, Shahdara, Delhi
# Certificate No.: DL0820920060023881
# Date: 03/05/2023
# This is to certify that I/we have carefully examined Shri Krishna Agarwal, Son of Shri Yogesh Kumar, Date of Birth 08/07/2006, Age 16, Male, Registration No. 0708/00000/2212/0734922, resident of House No. 1/11110, Street No-9, Near Kirti Mandir, West Subhash Park, Shahdara, East Delhi, Delhi 110032, Sub District Shahdara, District Shahdara, State / UT Delhi, whose photograph is affixed above, and I am/we are satisfied that:
# (A) He is a case of Intellectual Disability
# (B) The diagnosis in his case is Severe Intellectual Impairment
# (C) He has 90% (in figure) Ninety percent(in words) Temporary Disability in relation to his Brain as per the guidelines (Guidelines for the purpose of assessing the extent of specified disability in a person included under RPWD Act, 2016 notified by Government of India vide S.O. 76(E) dated 04/01/2018).
# This certificate recommended for 1 year(s) 2 month(s), and therefore this certificate shall be valid till 03/07/2024
# The applicant has submitted the following document(s) as proof of residence:
# Nature of Document(s): Aadhaar card
# Signature / Thumb Impression of the Person with Disability
# Dr. UDAY KUMAR SINHA
# Regn. No.A-000826 (RC) Additional Professor
# Department of Clinical Psychology Dr. Anggawat HBAS, Delhi-110095
# """

# # Extract schema dynamically
# output_schema = extract_dynamic_schema(input_text)
# print(output_schema)

import spacy
from sentence_transformers import SentenceTransformer, util
from typing import List, Dict
import re
from datetime import datetime

class UniversalExtractor:
    def __init__(self, transformer_model="sentence-transformers/paraphrase-xlm-r-multilingual-v1"):
        self.model = SentenceTransformer(transformer_model)
        self.nlp = spacy.blank("en")  # SpaCy pipeline (can be extended for multilingual use)

    def extract_candidates(self, text: str) -> List[str]:
        """Extract entities or candidates from text."""
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents] or text.split("\n")  # Fallback: lines in text

    def semantic_match(self, schema: Dict[str, str], candidates: List[str]) -> Dict[str, str]:
        """Map extracted candidates to schema keys using semantic similarity."""
        schema_keys = list(schema.keys())
        schema_embeddings = self.model.encode(schema_keys, convert_to_tensor=True)
        candidate_embeddings = self.model.encode(candidates, convert_to_tensor=True)

        # Compute cosine similarities
        similarities = util.cos_sim(schema_embeddings, candidate_embeddings)

        # Find the best match for each schema key
        mapping = {}
        for i, schema_key in enumerate(schema_keys):
            best_match_idx = similarities[i].argmax().item()
            mapping[schema_key] = candidates[best_match_idx]
        return mapping

    def format_output(self, schema: Dict[str, str], matched_entities: Dict[str, str]) -> Dict[str, any]:
        """Format matched entities to align with schema types."""
        output = {}
        for key, value_type in schema.items():
            value = matched_entities.get(key, "").strip()
            if "date" in value_type.lower():
                output[key] = self.format_date(value)
            elif value_type == "number":
                output[key] = int(re.sub(r"[^\d]", "", value)) if re.search(r"\d", value) else None
            elif value_type == "boolean":
                output[key] = value.lower() in ["true", "yes", "verified"]
            else:
                output[key] = value
        return output

    @staticmethod
    def format_date(date_string: str) -> str:
        """Try to parse and format dates dynamically."""
        for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%d %B %Y"):
            try:
                return datetime.strptime(date_string, fmt).strftime("%d/%m/%Y")
            except ValueError:
                continue
        return date_string  # Return as is if parsing fails

    def extract(self, text: str, schema: Dict[str, str]) -> Dict[str, any]:
        """Main extraction pipeline."""
        candidates = self.extract_candidates(text)
        matched_entities = self.semantic_match(schema, candidates)
        return self.format_output(schema, matched_entities)

# Example 1: Schema and Input Text
schema_birth = {
    "certificate_no": "string",
    "date": "date",
    "name": "string",
    "father_name": "string",
    "mother_name": "string",
    "date_of_birth": "date",
    "address": "string",
    "birth_place": "string",
    "registration_no": "string",
    "issued_date": "date"
}

text_birth = """
This is to certify that the following information is true and correct to the best of our knowledge and records. Sarah Emily Johnson, born on the 12th day of March 2010, was delivered at St. Mary’s Hospital, located in Los Angeles, California, USA. She is the legitimate child of Mr. John Alexander Johnson and Mrs. Elizabeth Grace Johnson, both residents of 78 Park Avenue, Los Angeles. The birth was registered under Registration No: BIRTH/2010/LA56789, and this certificate is issued under Certificate No: BC-3456789. The child’s details were verified based on hospital and municipal records, and the birth is officially registered in the Los Angeles Municipality Office. This certificate is issued on the 15th day of March 2010.
"""

# Example 2: Schema and Input Text
schema_disability = {
    "certificate_no": "string",
    "date": "date",
    "name": "string",
    "father_name": "string",
    "date_of_birth": "date",
    "age": "number",
    "gender": "string",
    "registration_no": "string",
    "address": "string",
    "sub_district": "string",
    "district": "string",
    "state_ut": "string",
    "disability_type": "string",
    "diagnosis": "string",
    "disability_percentage": "number",
    "valid_until": "date",
    "document_type": "string",
    "medical_authority_name": "string",
    "medical_authority_reg_no": "string",
    "designation": "string",
    "institution_name": "string",
    "institution_address": "string"
}

text_disability = """
सत्यमेव जमी
Certificate No.: DL0820920060023881
Date: 03/05/2023
This is to certify that I/we have carefully examined Shri Krishna Agarwal, Son of Shri Yogesh Kumar, Date of Birth 08/07/2006, Age 16, Male, Registration No. 0708/00000/2212/0734922, resident of House No. 1/11110, Street No-9, Near Kirti Mandir, West Subhash Park, Shahdara, East Delhi, Delhi 110032, Sub District Shahdara, District Shahdara, State / UT Delhi.
"""

# Extractor Initialization
extractor = UniversalExtractor()

# Run Extraction
output_birth = extractor.extract(text_birth, schema_birth)
output_disability = extractor.extract(text_disability, schema_disability)

# Print Results
import json
print("Birth Certificate Extraction:")
print(json.dumps(output_birth, indent=4))

print("\nDisability Certificate Extraction:")
print(json.dumps(output_disability, indent=4))
