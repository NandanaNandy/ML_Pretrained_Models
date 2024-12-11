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
   "NT REGISTER NO. 103 1710484361 TAMIL பன்னியின் பெயர் / NAME OF THE SCHOOL ( 41 \ PBR413 \ 4122 ) ராஜவிக்னேஷ் மேல்நிலைப் பள்ளி மேலமாத்துர் அஆலத்தூர் (வ/பெரம்பலூர் R AJAVIGNESH HR SEC SCHOOL MELAMATHUR PO PERAMBALUR DT றப்பினா செயலா ். 2001150 யாநிலப் பள்ளித் தோவுகள் குழுமம் (மேலநிலை), தமிழ்நாடு தோவரின் மக்கொயாப்பம் MEMBER SECRETARY SIGNATURE OF THE CANDIDATE STATE BOARD OF SCHOOL EXAMINATIONS (HR SEC), TAMILNADU"
]

# Process the input data
output = extract_entity_relationships_to_json(texts)

# Output the result in pretty JSON format
print(json.dumps(output, indent=4))
