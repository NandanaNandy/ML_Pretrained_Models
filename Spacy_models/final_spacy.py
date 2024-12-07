# # import spacy

# # # Load spaCy's language model
# # nlp = spacy.blank("en")  # Using a blank model to preprocess for now

# # def preprocess_text(ocr_text):
# #     """
# #     Clean and preprocess OCR text.
# #     """
# #     # Replace newline characters with spaces
# #     text = ocr_text.replace("\n", " ").strip()
    
# #     # Remove extra spaces
# #     text = " ".join(text.split())
    
# #     # Normalize common OCR errors (e.g., misrecognized characters)
# #     replacements = {
# #         "0f": "of",
# #         "Mo": "No",
# #         "KS": "K.S.",
# #     }
# #     for old, new in replacements.items():
# #         text = text.replace(old, new)
    
# #     return text

# # # Sample OCR text
# # ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""
# # cleaned_text = preprocess_text(ocr_text)
# # print("Cleaned Text:", cleaned_text)

# # import re

# # def define_parameter_patterns():
# #     """
# #     Define regex patterns for parameter extraction.
# #     """
# #     patterns = {
# #         "Name": r"Name[: ]+([A-Za-z ]+)",
# #         "Date of Birth": r"Date of Birth[: ]+(\d{2}-[A-Za-z]{3}-\d{4})",
# #         "Register Number": r"Register Number[: ]+(\d+)",
# #         "Institution": r"Name & Address of the Institution[: ]+([A-Za-z ,]+)",
# #         "Total Marks": r"Total Marks[: ]+(\d+)",
# #         "Percentage": r"Percentage[: ]+(\d{1,2}\.\d{2})",
# #     }
# #     return patterns

# # # Example usage
# # patterns = define_parameter_patterns()
# # print("Defined Patterns:", patterns)
# # def extract_parameters_spacy(text, patterns):
# #     """
# #     Extract parameters using spaCy and regex patterns.
# #     """
# #     # Process text with spaCy
# #     doc = nlp(text)
    
# #     extracted = {}
# #     for param, pattern in patterns.items():
# #         match = re.search(pattern, doc.text, re.IGNORECASE)
# #         if match:
# #             extracted[param] = match.group(1)
    
# #     return extracted

# # # Combine Steps
# # patterns = define_parameter_patterns()
# # parameters = extract_parameters_spacy(cleaned_text, patterns)

# # print("Extracted Parameters:", parameters)
# # ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""

# # # Step 1: Preprocess
# # cleaned_text = preprocess_text(ocr_text)

# # # Step 2: Define Patterns
# # patterns = define_parameter_patterns()

# # # Step 3: Extract Parameters
# # parameters = extract_parameters_spacy(cleaned_text, patterns)

# # print("Final Extracted Parameters:", parameters)    

# import re
# import spacy

# # Load spaCy's language model (lightweight for text processing)
# nlp = spacy.blank("en")

# def preprocess_text(ocr_text):
#     """
#     Clean and preprocess OCR text.
#     """
#     # Replace newline characters with spaces
#     text = ocr_text.replace("\n", " ").strip()
    
#     # Remove extra spaces
#     text = " ".join(text.split())
    
#     # Normalize common OCR errors (add more as needed)
#     replacements = {
#         "0f": "of",
#         "Mo": "No",
#         "KS": "K.S.",
#     }
#     for old, new in replacements.items():
#         text = text.replace(old, new)
    
#     return text

# def define_parameter_patterns():
#     """
#     Define regex patterns for parameter extraction.
#     """
#     patterns = {
#         # Match name after "Name of Student" or "Name"
#         "Name": r"Name(?: of Student)?[: ]+([A-Za-z ]+)",
#         # Match date in DD-MMM-YYYY format after "Date of Birth"
#         "Date of Birth": r"Date of Birth[: ]+(\d{2}-[A-Za-z]{3}-\d{4})",
#         # Match register number
#         "Register Number": r"Register Number[: ]+(\d+)",
#         # Match institution name after "Name & Address of the Institution"
#         "Institution": r"Name & Address of the Institution[: ]+([\w .,]+)",
#         # Match total marks after "Total Marks"
#         "Total Marks": r"Total Marks[: ]+(\d+)",
#         # Match percentage after "Percentage"
#         "Percentage": r"Percentage[: ]+(\d{1,3}\.\d{2})",
#     }
#     return patterns

# def extract_parameters_spacy(text, patterns):
#     """
#     Extract parameters using spaCy and regex patterns.
#     """
#     # Process text with spaCy
#     doc = nlp(text)
    
#     extracted = {}
#     for param, pattern in patterns.items():
#         match = re.search(pattern, doc.text, re.IGNORECASE)
#         if match:
#             extracted[param] = match.group(1).strip()
    
#     return extracted

# # Sample OCR text
# ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""

# # Step 1: Preprocess
# cleaned_text = preprocess_text(ocr_text)

# # Step 2: Define Patterns
# patterns = define_parameter_patterns()

# # Step 3: Extract Parameters
# parameters = extract_parameters_spacy(cleaned_text, patterns)

# print("Extracted Parameters:", parameters)

# import re
# import spacy

# # Load spaCy's language model
# nlp = spacy.blank("en")

# def preprocess_text(ocr_text):
#     """
#     Clean and preprocess OCR text.
#     """
#     # Replace newline characters with spaces
#     text = ocr_text.replace("\n", " ").strip()
    
#     # Remove extra spaces
#     text = " ".join(text.split())
    
#     return text

# def define_parameter_patterns():
#     """
#     Define regex patterns for parameter extraction.
#     """
#     patterns = {
#         # Match name after "Name of Student"
#         "Name": r"Name 0f Student[: ]+([A-Za-z ]+)",
#         # Match date of birth in DD-MMM-YYYY format after "Date of Birth"
#         "Date of Birth": r"Date of Birth[: ]+(\d{2}-[A-Za-z]{3}-\d{4})",
#         # Match register number
#         "Register Number": r"Register Number[: ]+(\d+)",
#         # Match total marks
#         "Total Marks": r"Total Marks[: ]+(\d+)",
#         # Match percentage
#         "Percentage": r"Percentage[: ]+(\d{1,3}\.\d{2})",
#     }
#     return patterns

# def extract_parameters_spacy(text, patterns):
#     """
#     Extract parameters using spaCy and regex patterns.
#     """
#     # Process text with spaCy
#     doc = nlp(text)
    
#     extracted = {}
#     for param, pattern in patterns.items():
#         match = re.search(pattern, doc.text, re.IGNORECASE)
#         if match:
#             extracted[param] = match.group(1).strip()
    
#     return extracted

# # Exact OCR text you provided
# ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""


# # Step 1: Preprocess
# cleaned_text = preprocess_text(ocr_text)

# # Step 2: Define Patterns
# patterns = define_parameter_patterns()

# # Step 3: Extract Parameters
# parameters = extract_parameters_spacy(cleaned_text, patterns)

# print("Extracted Parameters:", parameters)











# import re
# import spacy

# # Load spaCy's language model
# nlp = spacy.blank("en")

# def preprocess_text(ocr_text):
#     """
#     Clean and preprocess OCR text.
#     """
#     # Replace newline characters with spaces
#     text = ocr_text.replace("\n", " ").strip()
    
#     # Remove extra spaces
#     text = " ".join(text.split())
    
#     # Fix common OCR errors
#     replacements = {
#         "0f": "of",
#         "Mo": "No",
#         "Name 0f Student": "Name of Student",
#     }
#     for old, new in replacements.items():
#         text = text.replace(old, new)
    
#     return text

# def extract_parameter_by_context(text, key_phrase, context_length=50):
#     """
#     Extract a parameter's value by finding its key phrase and extracting nearby text.
#     """
#     match = re.search(key_phrase, text, re.IGNORECASE)
#     if match:
#         # Get text following the key phrase
#         start = match.end()
#         context = text[start:start + context_length]
        
#         # Use spaCy to clean and extract the likely value
#         doc = nlp(context)
#         value = doc.text.strip().split()[0]  # Extract the first meaningful text
#         return value
#     return None

# def extract_all_parameters(text):
#     """
#     Extract all required parameters using regex and context-based parsing.
#     """
#     parameters = {}
    
#     # Extract name
#     parameters["Name"] = extract_parameter_by_context(text, r"Name of Student", context_length=30)
    
#     # Extract date of birth
#     parameters["Date of Birth"] = extract_parameter_by_context(text, r"Date of Birth", context_length=20)
    
#     # Extract register number
#     parameters["Register Number"] = extract_parameter_by_context(text, r"Register Number", context_length=20)
    
#     # Extract total marks
#     parameters["Total Marks"] = extract_parameter_by_context(text, r"Total Marks", context_length=20)
    
#     # Extract percentage
#     parameters["Percentage"] = extract_parameter_by_context(text, r"Percentage", context_length=20)
    
#     return parameters

# # Your OCR text
# ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""


# # Step 1: Preprocess
# cleaned_text = preprocess_text(ocr_text)

# # Step 2: Extract Parameters
# parameters = extract_all_parameters(cleaned_text)

# print("Extracted Parameters:", parameters)






import re
import spacy

# Load spaCy's blank language model
nlp = spacy.blank("en")

def preprocess_text(ocr_text):
    """
    Clean and preprocess OCR text to fix common errors.
    """
    # Replace newline characters with spaces
    text = ocr_text.replace("\n", " ").strip()
    
    # Remove extra spaces
    text = " ".join(text.split())
    
    # Fix common OCR errors
    replacements = {
        "0f": "of",
        "Mo": "No",
        "Name 0f Student": "Name of Student",
        "Kom": "Name",  # Fixing the specific typo in OCR text
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def extract_parameters(text):
    """
    Extract key parameters using regex and context-based parsing.
    """
    parameters = {}

    # Define patterns for key parameters
    patterns = {
        "Name": r"Name of Student[: ]+([A-Za-z ]+)",
        "Date of Birth": r"Date of Birth[: ]+([\d\-A-Za-z]+)",
        "Register Number": r"Register Number[: ]+(\d+)",
        "Total Marks": r"Total Marks[: ]+(\d+)",
        "Percentage": r"Percentage[: ]+([\d.]+)",
    }

    # Extract parameters using regex
    for param, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            parameters[param] = match.group(1).strip()

    # Special case: Handle name extraction when regex fails
    if "Name" not in parameters or not parameters["Name"]:
        name_match = re.search(r"Name[: ]+([A-Za-z ]+)\d", text)  # Look for name before a number
        if name_match:
            parameters["Name"] = name_match.group(1).strip()
    
    return parameters

# Your OCR text
import re
import spacy

# Load spaCy's blank language model
nlp = spacy.blank("en")

def preprocess_text(ocr_text):
    """
    Clean and preprocess OCR text to fix common errors.
    """
    # Replace newline characters with spaces
    text = ocr_text.replace("\n", " ").strip()
    
    # Remove extra spaces
    text = " ".join(text.split())
    
    # Fix common OCR errors
    replacements = {
        "0f": "of",
        "Mo": "No",
        "Name 0f Student": "Name of Student",
        "Kom": "Name",  # Fixing the specific typo in OCR text
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def extract_parameters(text):
    """
    Extract key parameters using regex and context-based parsing.
    """
    parameters = {}

    # Define patterns for key parameters
    patterns = {
        "Name": r"Name of Student[: ]+([A-Za-z ]+)",
        "Date of Birth": r"Date of Birth[: ]+([\d\-A-Za-z]+)",
        "Register Number": r"Register Number[: ]+(\d+)",
        "Total Marks": r"Total Marks[: ]+(\d+)",
        "Percentage": r"Percentage[: ]+([\d.]+)",
    }

    # Extract parameters using regex
    for param, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            parameters[param] = match.group(1).strip()

    # Special case: Handle name extraction when regex fails
    if "Name" not in parameters or not parameters["Name"]:
        name_match = re.search(r"Name[: ]+([A-Za-z ]+)\d", text)  # Look for name before a number
        if name_match:
            parameters["Name"] = name_match.group(1).strip()
    
    return parameters

# Your OCR text
ocr_text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""


# Step 1: Preprocess
cleaned_text = preprocess_text(ocr_text)

# Step 2: Extract Parameters
parameters = extract_parameters(cleaned_text)

# Step 3: Display results
print("Extracted Parameters:", parameters)
# Step 1: Preprocess
cleaned_text = preprocess_text(ocr_text)

# Step 2: Extract Parameters
parameters = extract_parameters(cleaned_text)

# Step 3: Display results
print("Extracted Parameters:", parameters)