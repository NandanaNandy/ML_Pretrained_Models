import re
from spellchecker import SpellChecker
import spacy

# Load spaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Initialize the spell checker
spell = SpellChecker()

def clean_text(text):
    """
    Remove unwanted characters, extra spaces, and line breaks from the text.
    """
    # Remove unwanted characters
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)
    
    # Remove extra spaces
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    return cleaned_text

def correct_spelling(text):
    """
    Correct common OCR errors using SpellChecker.
    """
    words = text.split()
    corrected_words = [spell.correction(word) if word else word for word in words]
    return " ".join(corrected_words)

def extract_and_validate_data(text):
    """
    Extract key data points from the OCR text using regex patterns and validate them.
    """
    extracted_data = {}

    # Example regex patterns for extracting structured data
    extracted_data["candidate_name"] = re.search(r"Name of Candidate[:\s]*([A-Za-z\s]+)", text)
    extracted_data["registration_number"] = re.search(r"Registration Number[:\s]*([\w-]+)", text)
    extracted_data["exam_paper"] = re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text)
    extracted_data["gate_score"] = re.search(r"GATE Score[:\s]*([\d.]+)", text)
    extracted_data["marks"] = re.search(r"Marks out of 100[:\s]*([\d.]+)", text)
    extracted_data["rank"] = re.search(r"All India Rank in this paper[:\s]*([\d]+)", text)
    extracted_data["validity_date"] = re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text)

    # Extract text from regex matches
    for key, match in extracted_data.items():
        if match:
            extracted_data[key] = match.group(1).strip()
        else:
            extracted_data[key] = None

    # Clean and correct the extracted data
    for key, value in extracted_data.items():
        if value:
            extracted_data[key] = clean_text(value)
            extracted_data[key] = correct_spelling(extracted_data[key])  # Apply spell correction

    return extracted_data

# Example noisy OCR text (as provided)
ocr_text = """GATE: GATE 2022 Scorecard Graduate Aptitude Test in Engineering Graduate Aptitude Test in Engineering (GATE) Name of Candidate MOHAMMAD WASIF ANSARI Parent's/Guardian's AKHTARI KHATOON Registration Number 1234567890 Examination Paper Computer Science and Information Technology (CS) GATE Score: 855 Marks out of 100: 63.33 All India Rank in this paper: 68 Valid up to 31st March 2025"""

# Clean the OCR text and extract key data
extracted_data = extract_and_validate_data(ocr_text)

# Print cleaned and structured data
print(extracted_data)
