import spacy
import json
import time

def extract_entity_relationships_to_json(texts):
    """
    Extract entities and their relationships from unstructured text data and output in the desired format.
    
    Parameters:
        texts (list): A list of unstructured text strings.
    
    Returns:
        dict: A dictionary containing entities in the specified format, along with the time taken to process.
    """
    nlp = spacy.load("en_core_web_sm")  # Load spaCy's pre-trained English model
    result = {"documents": []}  # Initialize the result structure
    
    start_time = time.time()  # Start the timer for performance measurement

    # Process texts in batches using nlp.pipe for efficiency
    for doc in nlp.pipe(texts, disable=["lemmatizer", "textcat"]):  # Disable unused components
        document_data = {
            "text": doc.text,
            "entities": [],
            "relationships": []
        }

        # Extract entities and their types
        for ent in doc.ents:
            entity_entry = {"entity": ent.text, "type": ent.label_}
            document_data["entities"].append(entity_entry)

        # Extract basic relationships (e.g., founder, born_in, etc.)
        for token in doc:
            if token.dep_ in ("nsubj", "dobj"):  # Subject or object dependency
                # Check if token's head is a named entity
                head_ent = [ent for ent in doc.ents if ent.start <= token.head.i < ent.end]
                if head_ent:
                    relationship = {
                        "entity1": {"text": token.text, "type": token.dep_},
                        "entity2": {"text": head_ent[0].text, "type": head_ent[0].label_},
                        "context": doc.text
                    }
                    document_data["relationships"].append(relationship)

        # Add the processed document to the results
        result["documents"].append(document_data)
    
    end_time = time.time()  # End the timer
    time_taken = end_time - start_time  # Calculate time taken for processing
    result["time_taken_seconds"] = round(time_taken, 2)  # Add the time taken to the result
    
    return result


# Example Input (Unstructured Data)
texts = [
   "GOVERNMENT OF TAMIL NADU ak pares 3, DIRECTORATE OF TECHNICAL EDUCATION ee Sy TAMIL NADU ENGINEERING ADMISSION - 2022 Application Number: 305994 Personal Information Name: RAJESH S Name of the Parent/Guardian: SARAVANAN S Communication Address: 107/D4, SOLARAJAPURAM STREET, Permanent Address: 107/D4, SOLARAJAPURAM STREET, AAVARAMPATTI, AAVARAMPATTI, RAJAPALAYAM - 626117 RAJAPALAYAM - 626117 State: Tamil nadu District; Virudhunagar Taluk: Rajapalayam Communication address pincode: 626117 Native District: Virudhunagar Civic status of Native Place: Municipality Date of Birth (DD-MM-YYYY): 15-04-2005 Gender: Male Mother Tongue: Tamil Nationality: Indian Nativity: Tamil nadu Religion: Hindu Name of the Community: BC Name of the Caste: Senaithalaivar, Senaikudiyar and Illaivaniar Aadhar Number (optional): 295206496531 Special Reservation Information Whether you are a candidate under quota for Eminent Sports person as per Ex-Servicemen (Only Army/Navy/ Air force services are Eligible): No annexure-ll, item No.22 of information brochure?: No Differently Abled Person: No Differently Abled Type: - TFC Center for certificate verification: PAC Ramasamy Raja's Polytechnic College,Rajapalayam - 626 108 Scholarship Information Parent Occupation: Self Employed Annual Income: 96000 Are you a First Graduate?: Yes Post Matric Scholarship (SC/SCA/ST/Converted Christians): No School of Study Information Category of School: Govt. Aided Civic status of school location (+2): Municipality Have you studied VIII to XII in Tamil Nadu?: Yes Have you studied from VI to VIII in private school under RTE and IX to XII in Government School?: No Have you studied VI to XII in Government school?: No Class Year of Passing Name of the schoo! District State Block Category of Govt.School VI Std. 2016 N.a Annapparaja Memorial H S S Ra- Virudhunagar Tamil nadu Rajapalayam - japalayam japalayam japalayam japalayam japalayam japalayam japalayam japalayam japalayam japalayam Academic Information Qualifying Examination: HSC Name of the Board of Examination: Tamil nadu Board of Higher Secondary Education Permanent register number: 2111119945 HSC Roll number: 5119714 Qualified Year: 2022 HSC Group: HSC Academic Group Code: Physics/ Chemistry/ Maths/ Biology Medium of Instruction: Tamil HSC maximum (total) marks: 600 HSC obtained marks: 513 SSLC maximum (total) marks: 500 SSLC obtained marks: 424 Have you applied for NEET ?: No Have you applied for JEE ?: No Educational Management Information System(EMIS) Number: Community certificate number: FFDB678C6A687B86 332606127 7500257"
]

# Process the input data
output = extract_entity_relationships_to_json(texts)

# Output the result in pretty JSON format
print(json.dumps(output, indent=4))
