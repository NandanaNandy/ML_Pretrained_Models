# import re
# import spacy
# import json
# import time
# from typing import Dict, List, Any, Optional
# from datetime import datetime
# import pytz
# import tracemalloc
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# class PerformanceDocumentExtractor:
#     def __init__(self, model_name: str = 'xx_ent_wiki_sm', enable_memory_profiling: bool = False):
       
#         try:
#             self.nlp = spacy.load(model_name)
#             logging.info(f"SpaCy model '{model_name}' loaded successfully.")
#         except Exception as e:
#             logging.error(f"Failed to load SpaCy model: {e}")
#             raise

#         self.enable_memory_profiling = enable_memory_profiling

#         # Extraction patterns
#         self.extraction_patterns = {
#             'name_patterns': [
#                 r'(?:Selvan|Thiru)\s+([A-Za-z\s]+)',
#                 r'Name\s*:?\s*([A-Za-z\s]+)',
#                 r'([A-Za-z\s]+)\s+(?:son|daughter)\s+of'
#             ],
#             'parent_patterns': [
#                 r'(?:son|daughter)\s+of\s+(Thiru\s+[A-Za-z\s]+)',
#                 r'Father\'s\s+Name\s*:?\s*([A-Za-z\s]+)',
#                 r'Parent\s*:?\s*([A-Za-z\s]+)'
#             ],
#             'address_patterns': [
#                 r'Door\s*(?:No)?\s*:?\s*(\d+/?\d*),?\s*([A-Za-z\s]+)\s+(?:of|in)\s+([A-Za-z\s]+)\s+(?:Village|Town|District)',
#                 r'Address\s*:?\s*([^\n]+)'
#             ]
#         }
    
#     def extract_entities_with_timing(self, text: str) -> Dict[str, Any]:
       
#         performance_metrics = {
#             'total_extraction_time': 0,
#             'method_timings': {}
#         }

#         total_start_time = time.time()
#         if self.enable_memory_profiling:
#             tracemalloc.start()

#         entities = {}

#         def timed_extraction(method, *args):
#             start_time = time.time()
#             start_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

#             result = method(*args)

#             end_time = time.time()
#             end_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

#             method_name = method.__name__
#             performance_metrics['method_timings'][method_name] = {
#                 'execution_time': end_time - start_time,
#                 'memory_used': (end_memory - start_memory) if start_memory is not None else 'Not tracked'
#             }

#             return result

#         entities['name'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['name_patterns'])
#         entities['parent_name'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['parent_patterns'])
#         entities['address'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['address_patterns'])

#         spacy_start_time = time.time()
#         spacy_start_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

#         doc = self.nlp(text)
#         spacy_entities = [
#             {
#                 'text': ent.text,
#                 'label': ent.label_,
#                 'start': ent.start_char,
#                 'end': ent.end_char
#             } for ent in doc.ents
#         ]

#         spacy_end_time = time.time()
#         spacy_end_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

#         performance_metrics['method_timings']['spacy_ner'] = {
#             'execution_time': spacy_end_time - spacy_start_time,
#             'memory_used': (spacy_end_memory - spacy_start_memory) if spacy_start_memory is not None else 'Not tracked'
#         }

#         total_end_time = time.time()
#         performance_metrics['total_extraction_time'] = total_end_time - total_start_time

#         if self.enable_memory_profiling:
#             tracemalloc.stop()

#         return {
#             'extracted_entities': entities,
#             'spacy_entities': spacy_entities,
#             'performance_metrics': performance_metrics
#         }
    
#     def extract_by_patterns(self, text: str, pattern_list: List[str]) -> Optional[str]:
       
#         for pattern in pattern_list:
#             match = re.search(pattern, text, re.IGNORECASE)
#             if match:
#                 return match.group(1).strip()
#         return None

# def main():
#     sample_texts = [
#         "GATE 2021 Scorecard GATE Graduate Aptitude Test in Engineering (GATE) 2 21 Bant Name MomAmm MOHAMMAD WASIF ANSARI 1 Parent's Guardian's Name Registration Number j Examination Paper Computer Science and Information Technology (CS) (H4 wastt Ansar (Candidate'$ Signature) GATE Score 678 Number of Candidates 101922 Appeared in this paper L Marks out of 100* 53.08 AII India Rank in this 943 paper Qualifying Marks"" 26.1 23.4 17.4 General EWSIOBC (NCL) scistipwD Valid up to 31 March 2024 Normalized   marks   for   Civil  Engineering (CE) Computer Science and Information Technology (CS) and Mechanical Engineering  (ME) Papers. A candidate is considered qualified if the marks 19 March 2021 secured are greater than or equal t0 the qualifying Prof: Deepankar Choudhury marks mentioned for the calegory for which valid Organising Chairperson, GATE 2021 category certificate applicable, produced along (on bchalf of NCB GATE: for MoE) c8ab9d9712/28d13332d51dcb608det5 with Ihis scorecard: The GATE 2021 score is calculated using the formula"

#     ]

#     extractor = PerformanceDocumentExtractor(enable_memory_profiling=True)

#     for i, text in enumerate(sample_texts, 1):
#         print(f"\n{'='*50}")
#         print(f"DOCUMENT {i} ENTITY EXTRACTION PERFORMANCE")
#         print(f"{'='*50}")
#         results = extractor.extract_entities_with_timing(text)

#         print("\n[1] EXTRACTED ENTITIES:")
#         print(json.dumps(results['extracted_entities'], indent=2))

#         print("\n[2] SPACY ENTITIES:")
#         print(json.dumps(results['spacy_entities'], indent=2))

#         print("\n[3] PERFORMANCE METRICS:")
#         perf_metrics = results['performance_metrics']
#         print(f"Total Extraction Time: {perf_metrics['total_extraction_time']:.6f} seconds")
#         print("\nMethod-wise Timings:")
#         for method, metrics in perf_metrics['method_timings'].items():
#             print(f"- {method}:")
#             print(f"  Execution Time: {metrics['execution_time']:.6f} seconds")
#             print(f"  Memory Used: {metrics['memory_used']} bytes")

# if __name__ == '__main__':
#     main()



#####   CODE 2
# import re
# import spacy
# import json
# import time
# from typing import Dict, List, Any, Optional
# import tracemalloc
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# class DynamicEntityExtractor:
#     def __init__(self, model_name: str = 'xx_ent_wiki_sm', enable_memory_profiling: bool = False):
#         """
#         Initialize the extractor with the SpaCy model and optional memory profiling.
#         """
#         try:
#             self.nlp = spacy.load(model_name)
#             logging.info(f"SpaCy model '{model_name}' loaded successfully.")
#         except Exception as e:
#             logging.error(f"Failed to load SpaCy model: {e}")
#             raise

#         self.enable_memory_profiling = enable_memory_profiling
#         self.custom_patterns: Dict[str, List[str]] = {}

#     def add_entity_patterns(self, entity_name: str, patterns: List[str]):
#         """
#         Add custom patterns for a specific entity type.
#         """
#         self.custom_patterns[entity_name] = patterns

#     def extract_entities(self, text: str, entity_types: List[str]) -> Dict[str, Any]:
#         """
#         Extract specified entities with detailed performance metrics.
#         """
#         performance_metrics = {'method_timings': {}, 'total_extraction_time': 0}
#         extracted_entities = {}
#         tracemalloc.start() if self.enable_memory_profiling else None
#         total_start_time = time.time()

#         # Timing wrapper
#         def timed_extraction(method, *args):
#             start_time = time.time()
#             start_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None
#             result = method(*args)
#             end_time = time.time()
#             end_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None
#             performance_metrics['method_timings'][method.__name__] = {
#                 'execution_time': end_time - start_time,
#                 'memory_used': (end_memory - start_memory) if start_memory is not None else 'Not tracked'
#             }
#             return result

#         # Extract custom entities via patterns
#         for entity in entity_types:
#             patterns = self.custom_patterns.get(entity, [])
#             extracted_entities[entity] = timed_extraction(self._extract_by_patterns, text, patterns)

#         # Use SpaCy for NER extraction
#         spacy_entities = timed_extraction(self._extract_with_spacy, text)

#         performance_metrics['total_extraction_time'] = time.time() - total_start_time
#         tracemalloc.stop() if self.enable_memory_profiling else None

#         return {
#             'extracted_entities': extracted_entities,
#             'spacy_entities': spacy_entities,
#             'performance_metrics': performance_metrics
#         }

#     def _extract_by_patterns(self, text: str, pattern_list: List[str]) -> Optional[str]:
#         """
#         Extract information using regex patterns.
#         """
#         for pattern in pattern_list:
#             match = re.search(pattern, text, re.IGNORECASE)
#             if match:
#                 return match.group(1).strip()
#         return None

#     def _extract_with_spacy(self, text: str) -> List[Dict[str, Any]]:
#         """
#         Extract entities using SpaCy's NER model.
#         """
#         doc = self.nlp(text)
#         return [{'text': ent.text, 'label': ent.label_, 'start': ent.start_char, 'end': ent.end_char} for ent in doc.ents]

# def main():
#     # Initialize extractor with memory profiling enabled
#     extractor = DynamicEntityExtractor(enable_memory_profiling=True)


#     extractor.add_entity_patterns('name', [
#         r'(?:Selvan|Thiru)\s+([A-Za-z\s]+)',
#         r'Name\s*:?\s*([A-Za-z\s]+)',
#         r'([A-Za-z\s]+)\s+(?:son|daughter)\s+of'
#     ])
#     extractor.add_entity_patterns('parent_name', [
#         r'(?:son|daughter)\s+of\s+(Thiru\s+[A-Za-z\s]+)',
#         r'Father\'s\s+Name\s*:?\s*([A-Za-z\s]+)',
#         r'Parent\s*:?\s*([A-Za-z\s]+)'
#     ])
#     extractor.add_entity_patterns('address', [
#         r'Door\s*(?:No)?\s*:?\s*(\d+/?\d*),?\s*([A-Za-z\s]+)\s+(?:of|in)\s+([A-Za-z\s]+)\s+(?:Village|Town|District)',
#         r'Address\s*:?\s*([^\n]+)'
#     ])

#     text = (
#         "This is to certify that Selvan Nareshkanna $ son of Thiru Shanmugam residing at Door No 164/5, "
#         "Periyar nagar of Harur Village / Town Harur Taluk Dharmapuri District of the State of Tamil Nadu belongs to "
#         "24 Manai Telugu Chetty Community, which is recognized as a Backward Class as per Government Order."
#     )

#     entities_to_extract = ['name', 'parent_name', 'address']

#     results = extractor.extract_entities(text, entities_to_extract)

#     print("\n[1] Extracted Entities:")
#     print(json.dumps(results['extracted_entities'], indent=2))

#     print("\n[2] SpaCy Entities:")
#     print(json.dumps(results['spacy_entities'], indent=2))

#     print("\n[3] Performance Metrics:")
#     perf_metrics = results['performance_metrics']
#     print(f"Total Extraction Time: {perf_metrics['total_extraction_time']:.6f} seconds")
#     print("\nMethod-wise Timings:")
#     for method, metrics in perf_metrics['method_timings'].items():
#         print(f"- {method}:")
#         print(f"  Execution Time: {metrics['execution_time']:.6f} seconds")
#         print(f"  Memory Used: {metrics['memory_used']} bytes")

# if __name__ == '__main__':
#     main()




# # CODE 3
# import re
# from datetime import datetime
# from langdetect import detect
# import spacy

# # Load your fine-tuned SpaCy model
# try:
#     nlp_fine_tuned = spacy.load("path_to_fine_tuned_model")  # Replace with your model's path
# except:
#     nlp_fine_tuned = spacy.load("xx_ent_wiki_sm")  # Fallback to multilingual SpaCy model

# # Preprocessing Function
# def clean_text(text):
#     text = re.sub(r"[^a-zA-Z\u0900-\u097F\u0B80-\u0BFF\u0C00-\u0C7F\u0D00-\u0D7F0-9\s.,:-]", " ", text)
#     text = re.sub(r"\s+", " ", text).strip()
#     return text

# # Language Detection
# def detect_language(text):
#     try:
#         return detect(text)
#     except Exception:
#         return "unknown"

# # Certificate Type Identification
# def identify_certificate_type(text):
#     keywords = {
#         "birth_certificate": ["birth", "father", "mother", "जन्म", "பிறப்பு", "ജനന", "జన్మ"],
#         "eq_certificate": ["mark sheet", "degree", "cgpa", "percentage", "मार्कशीट", "தகுதி", "പരീക്ഷ", "పట్టా"],
#         "dob_proof": ["date of birth proof", "dob", "जन्मतिथि", "பிறந்த தேதி", "ജനന തിയ്യതി", "పుట్టినతేది"],
#         "experience_certificate": ["experience", "to_date", "from_date", "अनुभव", "அனுபவம்", "അനുഭവം", "అనుభవం"],
#         "gate_score_card": ["gate", "score", "गेट", "முழு மதிப்பெண்", "മൂല്യനിർണ്ണയം", "గేట్"],
#         "category_proof": ["category", "obc", "sc", "st", "ews", "pwd", "श्रेणी", "பிரிவு", "വർഗ്ഗം", "వర్గం"],
#         "phd_certificate": ["phd", "university", "project", "published", "पीएचडी", "பிஎச்டி", "പിഎച്ച്ഡി", "పిహెచ్‌డీ"]
#     }
#     for cert_type, kw_list in keywords.items():
#         if any(kw.lower() in text.lower() for kw in kw_list):
#             return cert_type
#     return None

# # Schema Extraction Functions (Regex-Based Fallback)
# def extract_schema_with_regex(text, cert_type):
#     extractors = {
#         "birth_certificate": {
#             "name": re.search(r'name[:\s]*([\w\s]+)', text),
#             "age": re.search(r'age[:\s]*(\d+)', text),
#             "father_name": re.search(r'father(?:\'s)? name[:\s]*([\w\s]+)', text),
#             "mother_name": re.search(r'mother(?:\'s)? name[:\s]*([\w\s]+)', text),
#             "date_of_birth": re.search(r'date of birth[:\s]*(\d{2}-\d{2}-\d{4})', text)
#         },
#         # Add other certificate-specific regex patterns
#     }
#     return {
#         key: (match.group(1).strip() if match else None)
#         for key, match in extractors.get(cert_type, {}).items()
#     }

# # NER-Based Extraction
# def extract_entities_with_spacy(text, cert_type):
#     doc = nlp_fine_tuned(text)
#     entities = {}
#     for ent in doc.ents:
#         if ent.label_ == "PERSON" and "name" in cert_type:
#             entities["name"] = ent.text
#         elif ent.label_ == "DATE" and "dob" in cert_type:
#             entities["date_of_birth"] = ent.text
#         elif ent.label_ == "ORG" and cert_type in ["phd_certificate", "eq_certificate"]:
#             entities["university"] = ent.text
#     return entities

# # Combine NER and Regex Extraction
# def extract_certificate_data(text, cert_type):
#     ner_data = extract_entities_with_spacy(text, cert_type)
#     regex_data = extract_schema_with_regex(text, cert_type)
#     # Combine data, prioritizing NER-based results
#     return {**regex_data, **{k: v for k, v in ner_data.items() if v}}

# # Main Processing Function
# def process_certificate(text):
#     cleaned_text = clean_text(text)
#     language = detect_language(cleaned_text)

#     if language == "unknown":
#         return {"error": "Language could not be detected"}

#     print(f"Detected language: {language}")

#     cert_type = identify_certificate_type(cleaned_text)
#     if cert_type is None:
#         return {"error": "Certificate type could not be identified"}

#     extracted_data = extract_certificate_data(cleaned_text, cert_type)
#     return {
#         "language": language,
#         "certificate_type": cert_type,
#         "extracted_data": extracted_data
#     }

# # Example Usage
# if __name__ == "__main__":
#     sample_text = """
#     GATE 2021 Scorecard GATE Graduate Aptitude Test in Engineering (GATE) 2 21 Bant Name MomAmm MOHAMMAD WASIF ANSARI 1 Parent's Guardian's Name Registration Number j Examination Paper Computer Science and Information Technology (CS) (H4 wastt Ansar (Candidate'$ Signature) GATE Score 678 Number of Candidates 101922 Appeared in this paper L Marks out of 100* 53.08 AII India Rank in this 943 paper Qualifying Marks"" 26.1 23.4 17.4 General EWSIOBC (NCL) scistipwD Valid up to 31 March 2024 Normalized   marks   for   Civil  Engineering (CE) Computer Science and Information Technology (CS) and Mechanical Engineering  (ME) Papers. A candidate is considered qualified if the marks 19" March 2021 secured are greater than or equal t0 the qualifying Prof: Deepankar Choudhury marks mentioned for the calegory for which valid Organising Chairperson, GATE 2021 category certificate applicable, produced along (on bchalf of NCB GATE: for MoE) c8ab9d9712/28d13332d51dcb608det5 with Ihis scorecard: The GATE 2021 score is calculated using the formula

#     """
#     result = process_certificate(sample_text)
#     print(result)


# code4
# import re
# import spacy
# import time  # Import the time module

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def extract_schema_with_spacy_and_regex(text):
#     # Start time recording
#     start_time = time.time()

#     # Process the text using spaCy for NER
#     doc = nlp(text)

#     # Define a function to get entities from spaCy output
#     def get_entities(label):
#         return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

#     # Function to identify the certificate type based on the content of the text
#     def identify_certificate_type(text):
#         if 'GATE' in text and 'Score' in text:
#             return "gate_score_card"
#         elif 'birth' in text and 'certificate' in text:
#             return "birth_certificate"
#         elif 'degree' in text and 'certificate' in text:
#             return "eq_certificate"
#         elif 'marksheet' in text and ('10th' in text or '12th' in text):
#             return "marksheet_10th" if '10th' in text else "marksheet_12th"
#         elif 'disability' in text and 'certificate' in text:
#             return "pwd_certificate"
#         elif 'experience' in text and 'certificate' in text:
#             return "experience_certificate"
#         elif 'phd' in text and 'certificate' in text:
#             return "phd_certificate"
#         else:
#             return "unknown"  # Default fallback if no match found

#     # Automatically detect the certificate type
#     cert_type = identify_certificate_type(text)

#     # Define extractors with regex and spaCy entities
#     extractors = {
#         "gate_score_card": {
#             "candidate_name": re.search(r"Name[:\s]*([A-Z\s]+)", text),
#             "parent_name": re.search(r"Parent's Guardian's Name[:\s]*([A-Z\s]+)", text),
#             "registration_number": re.search(r"Registration Number[:\s]*([\w-]+)", text),
#             "exam_paper": re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text),
#             "gate_score": re.search(r"GATE Score[:\s]*([\d.]+)", text),
#             "marks": re.search(r"Marks out of 100[:\s]*([\d.]+)", text),
#             "rank": re.search(r"All India Rank[:\s]*([\d]+)", text),
#             "qualifying_marks": re.search(r"Qualifying Marks[:\s]*([\d.\s]+)", text),
#             "validity_date": re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text),
#             "candidate_name_spacy": get_entities("PERSON"),
#             "validity_date_spacy": get_entities("DATE"),
#         },
#         "birth_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "age": re.search(r"age[:\s]*(\d+)", text),
#             "father_name": re.search(r"father(?:\'s)? name[:\s]*([\w\s]+)", text),
#             "mother_name": re.search(r"mother(?:\'s)? name[:\s]*([\w\s]+)", text),
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "name_spacy": get_entities("PERSON"),
#             "date_of_birth_spacy": get_entities("DATE"),
#         },
#         "eq_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "degree": re.search(r"degree[:\s]*([\w\s]+)", text),
#             "cgpa": re.search(r"cgpa[:\s]*([\d.]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "class": re.search(r"class[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "date_of_birth_spacy": get_entities("DATE"),
#         },
#         "dob_proof": {
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "date_of_birth_spacy": get_entities("DATE"),
#             "name_spacy": get_entities("PERSON"),
#         },
#         "experience_certificate": {
#             "from_date": re.search(r"from[:\s]*(\d{4}-\d{2}-\d{2})", text),
#             "to_date": re.search(r"to[:\s]*(\d{4}-\d{2}-\d{2})", text),
#             "from_date_spacy": get_entities("DATE"),
#             "to_date_spacy": get_entities("DATE"),
#         },
#         "category_certificate": {
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "category_spacy": get_entities("ORG"),  # Example: for categories like PwD, OBC, SC
#         },
#         "phd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "university": re.search(r"university[:\s]*([\w\s]+)", text),
#             "title_of_project": re.search(r"title of project[:\s]*([\w\s]+)", text),
#             "no_of_paper_published": re.search(r"papers published[:\s]*(\d+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "university_spacy": get_entities("ORG"),
#         },
#         "marksheet_10th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "marks": re.search(r"marks obtained[:\s]*([\d]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "marksheet_12th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "marks": re.search(r"marks obtained[:\s]*([\d]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "pwd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "category_spacy": get_entities("ORG"),  # For example, PwD or specific categories
#         }
#     }

#     # Extract data using regex and spaCy for the specific certificate type
#     extracted_data = {}
#     for key, value in extractors.get(cert_type, {}).items():
#         if isinstance(value, list):  # If the value is a list (from spaCy entities)
#             extracted_data[key] = value
#         else:  # If the value is a regex match object
#             extracted_data[key] = (value.group(1).strip() if value else None)

#     # Add the detected certificate type
#     extracted_data["certificate_type"] = cert_type

#     # End time recording
#     end_time = time.time()

#     # Calculate the time taken
#     mapping_time = end_time - start_time
#     extracted_data["mapping_time_seconds"] = mapping_time

#     return extracted_data

# # Example usage
# text = """GATE 2021 Scorecard GATE Graduate Aptitude Test in Engineering..."""  # Your example input text
# extracted_data = extract_schema_with_spacy_and_regex(text)
# print(extracted_data)








# # code 5
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













# # code 5-2
# import re
# import spacy
# import time

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def extract_schema_with_spacy_and_regex(text):
#     start_time = time.time()

#     # Process the text using spaCy for Named Entity Recognition (NER)
#     doc = nlp(text)

#     # Define a function to get entities from spaCy output
#     def get_entities(label):
#         return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

#     # Define a function to clean the input text by removing extra spaces and irrelevant characters
#     def clean_text(text):
#         # Remove unwanted characters and excessive whitespace
#         text = text.lower()  # Convert to lowercase
#         cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)  # Remove special chars
#         cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove extra spaces
#         return cleaned_text

#     # Function to identify the certificate type based on the content of the text
#     def identify_certificate_type(text):
#         if 'GATE' in text and 'Score' in text:
#             return "gate_score_card"
#         elif 'birth' in text and 'certificate' in text:
#             return "birth_certificate"
#         elif 'degree' in text and 'certificate' in text:
#             return "eq_certificate"
#         elif 'marksheet' in text and ('10th' in text or '12th' in text):
#             return "marksheet_10th" if '10th' in text else "marksheet_12th"
#         elif 'disability' in text and 'certificate' in text:
#             return "pwd_certificate"
#         elif 'experience' in text and 'certificate' in text:
#             return "experience_certificate"
#         elif 'phd' in text and 'certificate' in text:
#             return "phd_certificate"
#         else:
#             return "unknown"  # Default fallback if no match found

#     # Automatically detect the certificate type
#     cert_type = identify_certificate_type(text)

#     # Define extractors with regex and spaCy entities
#     extractors = {
#         "gate_score_card": {
#             "candidate_name": re.search(r"Name of Candidate[:\s]*([A-Za-z\s]+)", text),
#             "parent_name": re.search(r"Parent's/Guardian's Name[:\s]*([A-Za-z\s]+)", text),
#             "registration_number": re.search(r"Registration Number[:\s]*([\w-]+)", text),
#             "exam_paper": re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text),
#             "gate_score": re.search(r"GATE Score[:\s]*([\d.]+)", text),
#             "marks": re.search(r"Marks out of 100[:\s]*([\d.]+)", text),
#             "rank": re.search(r"All India Rank[:\s]*([\d]+)", text),
#             "validity_date": re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text),
#             "candidate_name_spacy": get_entities("PERSON"),
#             "validity_date_spacy": get_entities("DATE"),
#         },
#         "birth_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "name_spacy": get_entities("PERSON"),
#             "date_of_birth_spacy": get_entities("DATE"),
#         },
#         "eq_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "degree": re.search(r"degree[:\s]*([\w\s]+)", text),
#             "cgpa": re.search(r"cgpa[:\s]*([\d.]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "class": re.search(r"class[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "degree_spacy": get_entities("ORG"),
#         },
#         "marksheet_10th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "marksheet_12th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "pwd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "category_spacy": get_entities("ORG"),
#         }
#     }

#     # Extract data using regex and spaCy for the specific certificate type
#     extracted_data = {}
#     for key, value in extractors.get(cert_type, {}).items():
#         if isinstance(value, list):  # If the value is a list (from spaCy entities)
#             extracted_data[key] = value
#         else:  # If the value is a regex match object
#             extracted_data[key] = (value.group(1).strip() if value else None)

#     # Add the detected certificate type
#     extracted_data["certificate_type"] = cert_type

#     # Clean up the extracted data fields
#     for key in extracted_data:
#         if isinstance(extracted_data[key], str):
#             extracted_data[key] = clean_text(extracted_data[key])

#     # Add processing time
#     elapsed_time = time.time() - start_time
#     extracted_data["processing_time"] = elapsed_time

#     return extracted_data

# # Example usage
# text = """Government of Andhra Pradesh CERTIFICATE FOR PERSON WITH DISABILITY Miautt under Ine authority vide 6 0 Me Na J1, Wo Cw & Dw Dapt_ Dated 01.12.20091 Medical Board: Government Hospital, Rajahmundry ID No.of Person with Disability: 04052320080106039 Date of Issue: 27/12/2010 This is certified that Shri Komarapu Salkumar Slo Srinivasa Rao, Male, age 8 years, resident of HNo # 2-139, Palathodu Habitation, Palathodu Village, Mandapeta Mandal, East Godavari District, suffering from Permanent disability of the following category:- Visual Impalrment. Sub-type of disability Blind ness Cause of Disability Congenital-BetterEve,Congenital-WorseEye. Right eye aphakia with optic atrophy Ieft eye optic atrophy. Re-assessment of this case is not recommended, Percentage of disability in his case Is 100%  [Hundred percent]: Identification Marks of Person with Dlsability: - aJA Mole On The Right Side Of The Chest b)Na m4lb Signature/Thumb Impression] of Person with Disability  Signature Signature Signature' Lk Dr, A AISWARYA RAJYALAKSHMI Dr, T.RAMESH KISHORE Dr: P, GOPI KRISHNA Designation: CIVIL ASST, Designation; Designation: DCHS, SURGEON SUPERINTENDENT, GH, RJY RAJAHMUNDRY Regn No 49935 Regn No 17520 Regn.No 13149 Note: This Is not valid for Medico-Legal cases."""

# extracted_data = extract_schema_with_spacy_and_regex(text)
# print(extracted_data)

















# import re
# import spacy
# import time

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def extract_schema_with_spacy_and_regex(text):
#     start_time = time.time()

#     # Process the text using spaCy for Named Entity Recognition (NER)
#     doc = nlp(text)

#     # Define a function to get entities from spaCy output
#     def get_entities(label):
#         return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

#     # Define a function to clean the input text by removing extra spaces and irrelevant characters
#     def clean_text(text):
#         # Remove unwanted characters and excessive whitespace
#         text = text.lower()  # Convert to lowercase
#         cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)  # Remove special chars
#         cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove extra spaces
#         return cleaned_text

#     # Function to identify the certificate type based on the content of the text
#     def identify_certificate_type(text):
#         print(f"Analyzing text: {text[:100]}...")  # Print the first 100 characters for debugging

#         # Use regular expressions for broader matching
#         if re.search(r"(GATE.*Score|Gate.*Score)", text):
#             return "gate_score_card"
#         elif re.search(r"(birth.*certificate)", text, re.IGNORECASE):
#             return "birth_certificate"
#         elif re.search(r"(degree.*certificate)", text, re.IGNORECASE):
#             return "eq_certificate"
#         elif re.search(r"(marksheet.*(10th|12th))", text, re.IGNORECASE):
#             return "marksheet_10th" if "10th" in text.lower() else "marksheet_12th"
#         elif re.search(r"(disability.*certificate)", text, re.IGNORECASE):
#             return "pwd_certificate"
#         elif re.search(r"(experience.*certificate)", text, re.IGNORECASE):
#             return "experience_certificate"
#         elif re.search(r"(phd.*certificate)", text, re.IGNORECASE):
#             return "phd_certificate"
#         else:
#             return "unknown"  # Default fallback if no match found
#         # Automatically detect the certificate type
#     cert_type = identify_certificate_type(text)

#     # Define extractors with regex and spaCy entities
#     extractors = {
#         "gate_score_card": {
#             "candidate_name": re.search(r"Name of Candidate[:\s]*([A-Za-z\s]+)", text),
#             "parent_name": re.search(r"Parent's/Guardian's Name[:\s]*([A-Za-z\s]+)", text),
#             "registration_number": re.search(r"Registration Number[:\s]*([\w-]+)", text),
#             "exam_paper": re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text),
#             "gate_score": re.search(r"GATE Score[:\s]*([\d.]+)", text),
#             "marks": re.search(r"Marks out of 100[:\s]*([\d.]+)", text),
#             "rank": re.search(r"All India Rank[:\s]*([\d]+)", text),
#             "validity_date": re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text),
#             "candidate_name_spacy": get_entities("PERSON"),
#             "validity_date_spacy": get_entities("DATE"),
#         },
#         "birth_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "name_spacy": get_entities("PERSON"),
#             "date_of_birth_spacy": get_entities("DATE"),
#         },
#         "eq_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "degree": re.search(r"degree[:\s]*([\w\s]+)", text),
#             "cgpa": re.search(r"cgpa[:\s]*([\d.]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "class": re.search(r"class[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "degree_spacy": get_entities("ORG"),
#         },
#         "marksheet_10th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "marksheet_12th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "pwd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "category_spacy": get_entities("ORG"),
#         }
#     }

#     # Extract data using regex and spaCy for the specific certificate type
#     extracted_data = {}
#     for key, value in extractors.get(cert_type, {}).items():
#         if isinstance(value, list):  # If the value is a list (from spaCy entities)
#             extracted_data[key] = value
#         else:  # If the value is a regex match object
#             extracted_data[key] = (value.group(1).strip() if value else None)

#     # Add the detected certificate type
#     extracted_data["certificate_type"] = cert_type

#     # Clean up the extracted data fields
#     for key in extracted_data:
#         if isinstance(extracted_data[key], str):
#             extracted_data[key] = clean_text(extracted_data[key])

#     # Add processing time
#     elapsed_time = time.time() - start_time
#     extracted_data["processing_time"] = elapsed_time

#     return extracted_data

# # Example usage
# text = """Department = Empowerment Persons with Disabilities, Ministry Social Justice and Empowerment; Government of India Disability Certificate Issuing Medical Authority, Buldhana Maharashtra Cerifcate 0H0420619680200284 Date: 19/03/2010 Tnis is t0 cerify tha: Ilve have Carefully examined Shri Shivgir Daulatgir Giri, Son of Snr Daulatgir Giri; Daze of Birth 10/09/1968, Age 52 Male Istariot Nc 2704/00000/2101/0264006 reeident Hcuee Nc At Katoda Post Gangalgaon 443201 Sub Distric: Chikhli, Dis-rict Buldhana Stte Maharasntra wnos) pnczoorpn afxed arove, anc |m/we are sa0isne3-nat; (A) He i5 2 Cise Locomotor Disability The d zgnosis OPERATED CASE OF LUMBER DISC WITA PARAPARESIS ICI He has 459/in figure) Forty Five percentiin words) Permanen: Disabilty in relation t0 nis 0E- -ne owideiines (Guidelines for the pirpcse aesessingte exnt specifed Cisability percn induded under APwD Act, 2016 nctine- oovemtimens Inzia vice5.0. 7G0E| cated 01/01/20181. pplicant has srbmitted tre fcllowiinz Jocumentie Droot reeiderre Nature Documentis ; hocnoor ciro S gnature Thumi Impression of the Person with Disability Signatory notifed Medica Atiorizy Memberls) Issuing Medical Authority 3u dnanz Manbrasnttz Utt @AFELNMaie Mejnlio Lerby Ie jbIy 0 lerein underol anEEIL IEL Crdie "ou aM JLPO= RCS Cftt OrE_"""

# extracted_data = extract_schema_with_spacy_and_regex(text)
# print(extracted_data)












# code7
# import re
# import spacy
# import time

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def extract_schema_with_spacy_and_regex(text):
#     start_time = time.time()

#     # Process the text using spaCy for Named Entity Recognition (NER)
#     doc = nlp(text)

#     # Define a function to get entities from spaCy output
#     def get_entities(label):
#         return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

#     # Define a function to clean the input text by removing extra spaces and irrelevant characters
#     def clean_text(text):
#         # Remove unwanted characters and excessive whitespace
#         text = text.lower()  # Convert to lowercase
#         cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)  # Remove special chars
#         cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove extra spaces
#         return cleaned_text

#     # Function to identify the certificate type based on the content of the text
#     def identify_certificate_type(text):
#         print(f"Analyzing text: {text[:100]}...")  # Print the first 100 characters for debugging

#         # Use regular expressions for broader matching
#         if re.search(r"(GATE.*Score|Gate.*Score)", text):
#             return "gate_score_card"
#         elif re.search(r"(birth.*certificate)", text, re.IGNORECASE):
#             return "birth_certificate"
#         elif re.search(r"(degree.*certificate)", text, re.IGNORECASE):
#             return "eq_certificate"
#         elif re.search(r"(marksheet.*(10th|12th))", text, re.IGNORECASE):
#             return "marksheet_10th" if "10th" in text.lower() else "marksheet_12th"
#         elif re.search(r"(disability.*certificate)", text, re.IGNORECASE):
#             return "pwd_certificate"
#         elif re.search(r"(experience.*certificate)", text, re.IGNORECASE):
#             return "experience_certificate"
#         elif re.search(r"(phd.*certificate)", text, re.IGNORECASE):
#             return "phd_certificate"
#         else:
#             return "unknown"  # Default fallback if no match found
#         # Automatically detect the certificate type
#     cert_type = identify_certificate_type(text)

#     # Define extractors with regex and spaCy entities
#     extractors = {
#         "pwd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "category_spacy": get_entities("ORG"),
#             "disability_percentage_spacy": get_entities("PERCENT"),
#         }
#     }

#     # Extract data using regex and spaCy for the specific certificate type
#     extracted_data = {}
#     for key, value in extractors.get(cert_type, {}).items():
#         if isinstance(value, list):  # If the value is a list (from spaCy entities)
#             extracted_data[key] = value
#         else:  # If the value is a regex match object
#             extracted_data[key] = (value.group(1).strip() if value else None)

#     # Add the detected certificate type
#     extracted_data["certificate_type"] = cert_type

#     # Clean up the extracted data fields
#     for key in extracted_data:
#         if isinstance(extracted_data[key], str):
#             extracted_data[key] = clean_text(extracted_data[key])

#     # Add processing time
#     elapsed_time = time.time() - start_time
#     extracted_data["processing_time"] = elapsed_time

#     return extracted_data

# # Example usage
# text = """Department = Empowerment Persons with Disabilities, Ministry Social Justice and Empowerment; Government of India Disability Certificate Issuing Medical Authority, Buldhana Maharashtra Cerifcate 0H0420619680200284 Date: 19/03/2010 Tnis is t0 cerify tha: Ilve have Carefully examined Shri Shivgir Daulatgir Giri, Son of Snr Daulatgir Giri; Daze of Birth 10/09/1968, Age 52 Male Istariot Nc 2704/00000/2101/0264006 reeident Hcuee Nc At Katoda Post Gangalgaon 443201 Sub Distric: Chikhli, Dis-rict Buldhana Stte Maharasntra wnos) pnczoorpn afxed arove, anc |m/we are sa0isne3-nat; (A) He i5 2 Cise Locomotor Disability The d zgnosis OPERATED CASE OF LUMBER DISC WITA PARAPARESIS ICI He has 459/in figure) Forty Five percentiin words) Permanen: Disabilty in relation t0 nis 0E- -ne owideiines (Guidelines for the pirpcse aesessingte exnt specifed Cisability percn induded under APwD Act, 2016 nctine- oovemtimens Inzia vice5.0. 7G0E| cated 01/01/20181. pplicant has srbmitted tre fcllowiinz Jocumentie Droot reeiderre Nature Documentis ; hocnoor ciro S gnature Thumi Impression of the Person with Disability Signatory notifed Medica Atiorizy Memberls) Issuing Medical Authority 3u dnanz Manbrasnttz Utt @AFELNMaie Mejnlio Lerby Ie jbIy 0 lerein underol anEEIL IEL Crdie "ou aM JLPO= RCS Cftt OrE_"""

# extracted_data = extract_schema_with_spacy_and_regex(text)
# print(extracted_data)



















# code8-spellchecker
# import re
# import spacy
# import time
# from spellchecker import SpellChecker

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")
# spell = SpellChecker()

# def extract_schema_with_spacy_and_regex(text):
#     start_time = time.time()

#     # Process the text using spaCy for Named Entity Recognition (NER)
#     doc = nlp(text)

#     # Define a function to get entities from spaCy output
#     def get_entities(label):
#         return [ent.text.strip() for ent in doc.ents if ent.label_ == label]

#     # Define a function to clean the input text by removing extra spaces and irrelevant characters
#     def clean_text(text):
#         # Remove unwanted characters and excessive whitespace
#         cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,;:!?&/-]", "", text)  # Remove special chars
#         cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()  # Remove extra spaces
#         return cleaned_text

#     # Function to identify the certificate type based on the content of the text
#     def identify_certificate_type(text):
#         if 'GATE' in text and 'Score' in text:
#             return "gate_score_card"
#         elif 'birth' in text and 'certificate' in text:
#             return "birth_certificate"
#         elif 'degree' in text and 'certificate' in text:
#             return "eq_certificate"
#         elif 'marksheet' in text and ('10th' in text or '12th' in text):
#             return "marksheet_10th" if '10th' in text else "marksheet_12th"
#         elif 'disability' in text and 'certificate' in text:
#             return "pwd_certificate"
#         elif 'experience' in text and 'certificate' in text:
#             return "experience_certificate"
#         elif 'phd' in text and 'certificate' in text:
#             return "phd_certificate"
#         else:
#             return "unknown"  # Default fallback if no match found

#     # Automatically detect the certificate type
#     cert_type = identify_certificate_type(text)

#     # Define extractors with regex and spaCy entities
#     extractors = {
#         "gate_score_card": {
#             "candidate_name": re.search(r"Name of Candidate[:\s]*([A-Za-z\s]+)", text),
#             "parent_name": re.search(r"Parent's/Guardian's Name[:\s]*([A-Za-z\s]+)", text),
#             "registration_number": re.search(r"Registration Number[:\s]*([\w-]+)", text),
#             "exam_paper": re.search(r"Examination Paper[:\s]*([A-Za-z\s]+)", text),
#             "gate_score": re.search(r"GATE Score[:\s]*([\d.]+)", text),
#             "marks": re.search(r"Marks out of 100[:\s]*([\d.]+)", text),
#             "rank": re.search(r"All India Rank[:\s]*([\d]+)", text),
#             "validity_date": re.search(r"Valid up to[:\s]*([\d\sA-Za-z]+)", text),
#             "candidate_name_spacy": get_entities("PERSON"),
#             "validity_date_spacy": get_entities("DATE"),
#         },
#         "birth_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "date_of_birth": re.search(r"date of birth[:\s]*(\d{2}-\d{2}-\d{4})", text),
#             "name_spacy": get_entities("PERSON"),
#             "date_of_birth_spacy": get_entities("DATE"),
#         },
#         "eq_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "degree": re.search(r"degree[:\s]*([\w\s]+)", text),
#             "cgpa": re.search(r"cgpa[:\s]*([\d.]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "class": re.search(r"class[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "degree_spacy": get_entities("ORG"),
#         },
#         "marksheet_10th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "marksheet_12th": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "roll_number": re.search(r"roll number[:\s]*([\w\d]+)", text),
#             "percentage": re.search(r"percentage[:\s]*([\d.]+)", text),
#             "board": re.search(r"board[:\s]*([\w\s]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "board_spacy": get_entities("ORG"),
#         },
#         "pwd_certificate": {
#             "name": re.search(r"name[:\s]*([\w\s]+)", text),
#             "category": re.search(r"category[:\s]*([\w\s]+)", text),
#             "disability_percentage": re.search(r"disability percentage[:\s]*([\d.]+)", text),
#             "name_spacy": get_entities("PERSON"),
#             "category_spacy": get_entities("ORG"),
#         }
#     }

#     # Extract data using regex and spaCy for the specific certificate type
#     extracted_data = {}
#     for key, value in extractors.get(cert_type, {}).items():
#         if isinstance(value, list):  # If the value is a list (from spaCy entities)
#             extracted_data[key] = value
#         else:  # If the value is a regex match object
#             extracted_data[key] = (value.group(1).strip() if value else None)

#     # Add the detected certificate type
#     extracted_data["certificate_type"] = cert_type

#     # Clean up the extracted data fields
#     for key in extracted_data:
#         if isinstance(extracted_data[key], str):
#             extracted_data[key] = clean_text(extracted_data[key])

#     # Correct spelling of extracted fields
#     def correct_spelling(text):
#         if text:
#             words = text.split()
#             corrected_words = [spell.correction(word) if word else word or word for word in words]  # Correct spelling for each word
#             corrected_words = [word if word is not None else "" for word in corrected_words]  # Ensure no None values in the list
#             return " ".join(corrected_words)  # Join the corrected words into a string
#         return ""  # Return an empty string if input is None

#     # Apply spelling correction
#     for key in extracted_data:
#         if isinstance(extracted_data[key], str):
#             extracted_data[key] = correct_spelling(extracted_data[key])  # Correct spelling

#     # Add processing time
#     elapsed_time = time.time() - start_time
#     extracted_data["processing_time"] = elapsed_time

#     return extracted_data

# # Example usage
# text = """GATE: GATE 2022 Scorecard Graduate Aptitude Test in Engineering Graduate Aptitude Test in Engineering (GATE) Name of Candidate MOHAMMAD WASIF ANSARI Parent's/Guardian's AKHTARI KHATOON Registration Number 1234567890 Examination Paper Computer Science and Information Technology (CS) GATE Score: 855 Marks out of 100: 63.33 All India Rank in this paper: 68 Valid up to 31st March 2025"""
# extracted_data = extract_schema_with_spacy_and_regex(text)
# print(extracted_data)
