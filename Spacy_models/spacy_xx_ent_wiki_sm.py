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
    # Load the multilingual named entity recognition model
    nlp = spacy.load("xx_ent_wiki_sm")  # Load the multilingual NER model
    
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
text = """
GOVERNMENT OF TAMIL NADU
ak pares 3, DIRECTORATE OF TECHNICAL EDUCATION
ee Sy TAMIL NADU ENGINEERING ADMISSION - 2022
Application Number: 305994
Personal Information
Name: RAJESH S Name of the Parent/Guardian: SARAVANAN S
Communication Address: 107/D4, SOLARAJAPURAM STREET, Permanent Address: 107/D4, SOLARAJAPURAM STREET,
AAVARAMPATTI, AAVARAMPATTI,
RAJAPALAYAM - 626117 RAJAPALAYAM - 626117
State: Tamil nadu District; Virudhunagar
Taluk: Rajapalayam Communication address pincode: 626117
Native District: Virudhunagar Civic status of Native Place: Municipality
Date of Birth (DD-MM-YYYY): 15-04-2005 Gender: Male
Mother Tongue: Tamil Nationality: Indian
Nativity: Tamil nadu Religion: Hindu
Name of the Community: BC Name of the Caste: Senaithalaivar, Senaikudiyar and Illaivaniar
Aadhar Number (optional): 295206496531
Special Reservation Information
Whether you are a candidate under quota for Eminent Sports person as per Ex-Servicemen (Only Army/Navy/ Air force services are Eligible): No
annexure-ll, item No.22 of information brochure?:
No
Differently Abled Person: No Differently Abled Type: -
"""

# Example usage
texts = [text]  # Wrap your single input text in a list
output_json = extract_entity_relationships_to_json(texts)

# Convert the result to a JSON string and print
print(json.dumps(output_json, indent=4))
