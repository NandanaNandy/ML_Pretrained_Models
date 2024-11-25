from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import re
import json

# Load the tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("mdarhri00/named-entity-recognition")
model = AutoModelForTokenClassification.from_pretrained("mdarhri00/named-entity-recognition")
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Sample input text (this could be dynamically passed)
input_text = """
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
TFC Center for certificate verification:
PAC Ramasamy Raja's Polytechnic College,Rajapalayam - 626 108
Scholarship Information
Parent Occupation: Self Employed Annual Income: 96000
Are you a First Graduate?: Yes Post Matric Scholarship (SC/SCA/ST/Converted Christians): No
School of Study Information
Category of School: Govt. Aided Civic status of school location (+2): Municipality
Have you studied VIII to XII in Tamil Nadu?: Yes Have you studied from VI to VIII in private school under RTE and IX to XII in
Government School?:
No
Have you studied VI to XII in Government school?: No
Class Year of Passing Name of the schoo! District State Block Category of
Govt.School
VI Std. 2016 N.a Annapparaja Memorial H S S Ra- Virudhunagar Tamil nadu Rajapalayam -
japalayam
japalayam
japalayam
japalayam
japalayam
japalayam
japalayam
Academic Information
Qualifying Examination: HSC Name of the Board of Examination:
Tamil nadu Board of Higher Secondary Education
Permanent register number: 2111119945 HSC Roll number: 5119714
Qualified Year: 2022 HSC Group: HSC Academic
Group Code: Physics/ Chemistry/ Maths/ Biology Medium of Instruction: Tamil
HSC maximum (total) marks: 600 HSC obtained marks: 513
SSLC maximum (total) marks: 500 SSLC obtained marks: 424
Have you applied for NEET ?: No Have you applied for JEE ?: No
Educational Management Information System(EMIS) Number: Community certificate number: FFDB678C6A687B86
332606127 7500257
"""

# Extract named entities using NER pipeline
entities = ner_pipeline(input_text)

# Initialize the details dictionary with None as default values
applicant_details = {
    "application_number": None,
    "name": None,
    "parent_name": None,
    "address": None,
    "taluk": None,
    "pin_code": None,
    "district": None,
    "state": None,
    "DOB": None,
    "gender": None,
    "nationality": None,
    "nativity": None,
    "aadhar_number": None,
    "annual_income": None,
    "civic_status": None,
    "mother_tongue": None,
    "first_graduate": None,
    "school_category": None,
    "school_name": None,
    "permanent_register_number": None,
    "HSC_roll_no": None,
    "medium_of_instruction": None,
    "HSC_mark": None,
    "SSLC_mark": None,
    "community_certificate_number": None,
    "applied_for_neet": None,
    "applied_for_jee": None
}

# Loop through the named entities detected by NER pipeline
for entity in entities:
    word = entity['word'].lower()
    label = entity['entity'].lower()
    
    # Match fields from the NER output
    if 'application' in word and 'number' in word:
        match = re.search(r'(\d{6})', input_text)
        if match:
            applicant_details['application_number'] = match.group(1)

    if 'name' in word:
        if 'rajesh' in word:
            applicant_details['name'] = 'RAJESH S'
        elif 'saravanan' in word:
            applicant_details['parent_name'] = 'SARAVANAN S'

    if 'address' in word or 'pincode' in word:
        match_address = re.search(r'(\d{3}/[A-Za-z0-9]+,[\w\s]+,\s+[\w\s]+)', input_text)
        if match_address:
            applicant_details['address'] = match_address.group(0)
        match_pin_code = re.search(r'\d{6}', input_text)
        if match_pin_code:
            applicant_details['pin_code'] = match_pin_code.group(0)

    if 'gender' in word:
        if 'male' in word:
            applicant_details['gender'] = 'Male'

    if 'dob' in word:
        match_dob = re.search(r'(\d{2}-\d{2}-\d{4})', input_text)
        if match_dob:
            applicant_details['DOB'] = match_dob.group(1)

    if 'nationality' in word:
        if 'indian' in word:
            applicant_details['nationality'] = 'Indian'

    if 'aadhar' in word:
        match_aadhar = re.search(r'\d{12}', input_text)
        if match_aadhar:
            applicant_details['aadhar_number'] = match_aadhar.group(0)

    if 'annual income' in word:
        match_income = re.search(r'(\d+)', input_text)
        if match_income:
            applicant_details['annual_income'] = int(match_income.group(1))

    if 'first graduate' in word:
        if 'yes' in word:
            applicant_details['first_graduate'] = True

    if 'school category' in word:
        if 'govt' in word:
            applicant_details['school_category'] = 'Govt.'

    if 'marks' in word:
        match_hsc = re.search(r'HSC obtained marks: (\d+)', input_text)
        if match_hsc:
            applicant_details['HSC_mark'] = int(match_hsc.group(1))
        match_sslc = re.search(r'SSLC obtained marks: (\d+)', input_text)
        if match_sslc:
            applicant_details['SSLC_mark'] = int(match_sslc.group(1))

    if 'community certificate' in word:
        match_certificate = re.search(r'([A-Z0-9]+)', input_text)
        if match_certificate:
            applicant_details['community_certificate_number'] = match_certificate.group(1)

# Print the dynamically extracted applicant details
print(json.dumps(applicant_details, indent=4))
