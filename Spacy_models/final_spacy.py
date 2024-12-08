import spacy
from spacy.training.example import Example
import random

# Step 1: Prepare Training Data
TRAIN_DATA = [
    (
        "Candidate name: John Doe. Date of birth: 15-07-1990. Total marks: 85%",
        {
            "entities": [
                (16, 24, "NAME"),       # "John Doe" as NAME
                (41, 51, "DOB"),        # "15-07-1990" as DOB
                (66, 68, "TOTAL_MARK")  # "85" as TOTAL_MARK
            ]
        }
    ),
    (
        "Name: Jane Smith, DOB: 22-09-1992, Marks: 92",
        {
            "entities": [
                (6, 16, "NAME"),
                (23, 33, "DOB"),
                (42, 44, "TOTAL_MARK")
            ]
        }
    ),
    # Add more examples for better accuracy
]

for entity in TRAIN_DATA:
    text, dataset = entity
    for start, end, label in dataset["entities"]:
        if start >= end:
            print(f"Invalid entity: {text[start:end]}")
        else:
            print(f"Entity: {text[start:end]}, Label: {label}")

exit()

# Step 2: Initialize the NLP Model
# Load a pre-trained model or create a blank one
nlp = spacy.load("en_core_web_lg")  # or spacy.blank("en") for a blank model

# Add the NER component to the pipeline if it's not already present
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Step 3: Add Labels to the NER Component
# Add custom labels to the NER component
for _, annotations in TRAIN_DATA:
    for ent in annotations["entities"]:
        ner.add_label(ent[2])

# Step 4: Train the Model
# Disable other pipeline components to focus on training the NER
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.initialize()  # Correct initialization
    for epoch in range(30):  # Adjust epochs as needed
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.5, losses=losses)  # Adjust drop rate if needed
        print(f"Losses at epoch {epoch}: {losses}")

# Step 5: Save the Trained Model
# Save the model to a directory
nlp.to_disk("custom_ner_model")
print("Model saved!")

# Step 6: Test the Model
# Load the trained model
custom_nlp = spacy.load("custom_ner_model")

# Test with new text
test_text = "Name: Jane Smith, DOB: 22-09-1992, Marks: 92"
doc = custom_nlp(test_text)

print("Entities found:")
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
