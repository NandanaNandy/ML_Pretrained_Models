# # Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="microsoft/Phi-3.5-mini-instruct", trust_remote_code=True)
# pipe(messages)

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3.5-mini-instruct", trust_remote_code=True)
import json
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("PrunaAI/EleutherAI-gpt-neo-1.3B-bnb-4bit-smashed")
model = AutoModelForCausalLM.from_pretrained("PrunaAI/EleutherAI-gpt-neo-1.3B-bnb-4bit-smashed")

# Define input unstructured text
unstructured_text = """
GOVERNMENT OF TAMIL NADU
DIRECTORATE OF TECHNICAL EDUCATION
Application Number: 305994
Name: RAJESH S
Name of the Parent/Guardian: SARAVANAN S
Communication Address: 107/D4, SOLARAJAPURAM STREET, RAJAPALAYAM - 626117
Permanent Address: 107/D4, SOLARAJAPURAM STREET, RAJAPALAYAM - 626117
State: Tamil Nadu
District: Virudhunagar
Date of Birth (DD-MM-YYYY): 15-04-2005
Gender: Male
Nationality: Indian
Aadhar Number: 295206496531
Annual Income: 96000
"""

# Tokenize the input
inputs = tokenizer(unstructured_text, return_tensors="pt")

# Generate model output
output_ids = model.generate(inputs['input_ids'], max_length=512)
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Function to extract JSON-like structure
def extract_json(text):
    try:
        # Find the JSON-like portion in the generated text
        json_start = text.find("{")
        json_end = text.rfind("}") + 1
        json_text = text[json_start:json_end]

        # Parse JSON
        structured_data = json.loads(json_text)
        return structured_data
    except Exception as e:
        print(f"Error extracting JSON: {e}")
        return None

# Get JSON formatted output
json_output = extract_json(generated_text)

# Print JSON
if json_output:
    print(json.dumps(json_output, indent=4))
else:
    print("Could not extract JSON from the output.")
