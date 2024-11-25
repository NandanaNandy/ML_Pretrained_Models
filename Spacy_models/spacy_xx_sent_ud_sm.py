import spacy

# Load the xx_sent_ud_sm model
nlp = spacy.load("xx_sent_ud_sm")

# Sample text in multiple languages
text = """This is to certify that Selvan Nareshkanna,  residing at Door No.
    164/5 Periyar Nagar, of Harur Village / Town Harur Taluk Dharmapuri District of the State of Tamil
    Nadu belongs to 24 Manai Telugu Chetty Community, which is recognized as a Backward Class as
    per Government Order (Ms.) No. 85, Backward Classes, Most Backward Classes and Minority Welfare
    Department (BCC), dated 29th July 2008 vide Serial No. 100.

    Signature Not Verified

    Digitally signed by A PALANISAMY
    Date: 01/02/2019 08:776:26 IST

    District : Dharmapuri
    Taluk : Harur"""

# Process the text
doc = nlp(text)

# Print sentences
print("Detected sentences:")
for sent in doc.sents:
    print(sent.text)

# Print token information
print("\nTokens and their dependencies:")
for token in doc:
    print(f"Token: {token.text}, Dependency: {token.dep_}, Head: {token.head.text}")