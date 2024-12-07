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
text = """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""

# Example usage
texts = [text]  # Wrap your single input text in a list
output_json = extract_entity_relationships_to_json(texts)

# Convert the result to a JSON string and print
print(json.dumps(output_json, indent=4))
