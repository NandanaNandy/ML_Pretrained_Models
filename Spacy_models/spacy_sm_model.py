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

text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""


process_text(text)
