# import re
# from spellchecker import SpellChecker

# # Function to clean noisy OCR text
# def clean_noisy_ocr_text(ocr_text):
#     # Replace common OCR misinterpretations (expand this list based on your OCR errors)
#     corrections = {
#         'O': '0',  # O to 0
#         'l': '1',  # l to 1
#         'I': '1',  # I to 1
#         'S': '5',  # S to 5
#         'B': '8',  # B to 8
#         'U': 'V',  # U to V
#         'Z': '2',  # Z to 2
#         'A': '@',  # A to @
#         # Add other OCR-specific corrections here
#     }

#     # Replace corrections
#     for misread, correct in corrections.items():
#         ocr_text = ocr_text.replace(misread, correct)

#     # Remove unwanted characters (non-alphanumeric, unwanted punctuation, etc.)
#     ocr_text = re.sub(r'[^A-Za-z0-9\s]', '', ocr_text)

#     # Normalize spaces and remove excess whitespace
#     ocr_text = ' '.join(ocr_text.split())

#     # Correct spelling using a spell checker
#     spell = SpellChecker()
#     words = ocr_text.split()
#     corrected_words = []

#     for word in words:
#         corrected = spell.correction(word)
#         if corrected:
#             corrected_words.append(corrected)  # Add the corrected word
#         else:
#             corrected_words.append(word)  # If no correction, keep the original word

#     ocr_text = ' '.join(corrected_words)

#     return ocr_text

# # Example usage
# ocr_text = "தமிழநாடு மாநிலப் பள்ளிக் தே STATE BOARD OF SCHOOL EXAMINATION: வரசுத் தேர்வுகள் துறை, சென்னை DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNA மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு மதிப்பெ HIGHER SECONDARY COURSE - SECOND YEAR WARK CER நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வரங்கப்படுக் ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU மதிப்பெண் சான்றிது தேர்வரின் பெயர் / NAME OF THE CANDIDATE வம்புகள் பட்ட பருக நடர்வுகண்ணா ச pinill curril to SESSIO AND YEAR OF ISSUE OF NARESHKANNA S MARK CERTIFICATE நிரந்தரப் பதிவெண் / PERMANENT REGISTER NUMBER பிறந்த தேசி / DATE OF BIRTH ம் 2022 26/04/2005 2111357078 MAY 2022 கழக்குறிப்பிட்டுள்ள மலநிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு பொதுத் தேர்வெழுதிய மேற்காண் தேர்வா ாடங்களில் தேர்வெழுதி தேர்ச்சி பெற்றுள்ளார் எனச் சான்றளிக்கப்படுகிறது. Certified that the above mentioned candidate passed the following subjects in the Higher Secondary Second Year Examination. தேர்ச்சி பெற்ற பருவம், வருடம் பெற்ற அகமதிப்பீடு கருத்தியல் செய்முறை பா 16 மதிப்பெண்கள் 100 க்கு INTERNAL மற்றும் தேர்வெண் THEORY PRACTICAL SUBJECT MARKS SESSION, YEAR AND 70/90 10/25 20/75 OBTAINED FOR 100 ROLL NO, OF PASSING கமிழ் 5357306 MAY 2022 072 010 082 TAMIL ஆங்கிலம் 5357306 MAY 2022 070 080 010 ENGLISH இயற்பியல் 5357306 MAY 2022 039 020 010 069 PHYSICS வேதியியல் 087 5357306 MAY 2022 057 020 010 CHEMISTRY உயிரியல் 5357306 MAY 2022 045 020 010 075 BIOLOGY கணிதவியல் 049 010 059 5357306 MAY 2022 MATHEMATICS மொத்த மதிப்பெண்கள் / TOTAL MARKS : 0452 ZERO FOUR FIVE TWO பள்ளியின் பெயர் / SCHOOL NAME ( 055/TCGE0098/055026 ) J K K NATTRAJA MATRIC HR SEC SCHOOL KOMARAPALAYAM ஜே.கே. கே.நடராஜா மெட்ரிக் மேல்நிலைப்பள்ளி பயிற்றுமொழி / MEDIUM OF INSTRUCTION பாடத்தொகுப்பு எண் மற்றும் பெயர் / GROUP CODE AND NAME ENGLISH பொதுக்கல்வி / GENERAL EDUCATION அ.ம.ப. குறிமீட்டெண் & நாள் / T.M.R.CODE NO.& DATE 2503 A2324947 20.06.2022 EMIS ID No. 3305080910201800 மாநிலப் பள்ளித் தோவுகள் குழுமம் (மேலநிலை) தமிழ்நாடு MEMBER SECRETARY STATE BOARD OF SCHOOL EXAMINATIONS (HR SEC) TAMILNADU ் கிரிக்க ் கிரிக்கி குறிக்கும் குறிக்கும் குறிக்க"
# cleaned_text = clean_noisy_ocr_text(ocr_text)
# print("Cleaned Text:", cleaned_text)

# # import re

# # # Function to clean noisy Tamil OCR text
# # def clean_tamil_ocr_text(ocr_text):
# #     # Replace common OCR misinterpretations
# #     corrections = {
# #         '௧': '1',  # Tamil digits (e.g., ௧ to 1)
# #         '௨': '2',  # Tamil digits (e.g., ௨ to 2)
# #         '௩': '3',  # Tamil digits (e.g., ௩ to 3)
# #         '௪': '4',  # Tamil digits (e.g., ௪ to 4)
# #         '௫': '5',  # Tamil digits (e.g., ௫ to 5)
# #         '௬': '6',  # Tamil digits (e.g., ௬ to 6)
# #         '௭': '7',  # Tamil digits (e.g., ௭ to 7)
# #         '௮': '8',  # Tamil digits (e.g., ௮ to 8)
# #         '௯': '9',  # Tamil digits (e.g., ௯ to 9)
# #         'ஓ': 'O',  # OCR errors in vowel recognition
# #         'கா': 'க',  # OCR misrecognizing letters
# #         'ஆ': 'அ',
# #         'இ': 'I',
# #         'ஊ': 'U',
# #         'கொ': 'க',  # Remove unwanted joined letters
# #         'அம்': 'ம்',
# #         'அண்ணா': 'அண்ணா',  # Correcting specific words if necessary
# #         'செய்ய': 'செய்ய',
# #         'ஈ': 'இ',  # OCR error corrections
# #         # Add more specific corrections as needed
# #     }

# #     # Replace corrections
# #     for misread, correct in corrections.items():
# #         ocr_text = ocr_text.replace(misread, correct)

# #     # Remove unwanted characters (non-alphanumeric, unwanted punctuation, etc.)
# #     ocr_text = re.sub(r'[^A-Za-z0-9\s\U0000B80-\U0000BFF0\U0000BBF0-\U0000BBFF]', '', ocr_text)  # Keep Tamil characters, numbers, and spaces

# #     # Normalize spaces and remove excess whitespace
# #     ocr_text = ' '.join(ocr_text.split())

# #     return ocr_text

# # # Example usage
# # ocr_text = """தமிழநாடு மாநிலப் பள்ளிக் தே STATE BOARD OF SCHOOL EXAMINATION: வரசுத் தேர்வுகள்..."""
# # cleaned_text = clean_tamil_ocr_text(ocr_text)
# # print("Cleaned Text:", cleaned_text)


import re
import spacy

# Load spaCy's blank language model
nlp = spacy.blank("xx")  # "xx" for multi-language processing

def preprocess_multilang_text(ocr_text):
    """
    Clean and preprocess OCR text for multiple languages (e.g., Tamil, Hindi, English).
    """
    # Replace newline characters with spaces
    text = ocr_text.replace("\n", " ").strip()
    
    # Remove extra spaces
    text = " ".join(text.split())
    
    # Fix common OCR errors for multi-language text
    replacements = {
        # Generic replacements
        "0f": "of",  # Common OCR mistake in English
        "Mo": "No",
        # Language-specific replacements
        "नाम": "नाम",  # Example Hindi text for 'Name'
        "பெயர்": "பெயர்",  # Tamil word for 'Name'
        "कुल": "कुल",  # Hindi for 'Total'
        "மொத்த": "மொத்த",  # Tamil for 'Total'
        # Add more corrections as needed for specific languages
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

# Example OCR texts in multiple languages
ocr_text_english = "Name 0f Student: RAMESH P N\nTotal Marks: 2002"
ocr_text_tamil = "பெயர்: ரமேஷ் P N\nமொத்த மதிப்பெண்கள்: 2002"
ocr_text_hindi = "नाम: रमेश P N\nकुल अंक: 2002"

# Preprocess the texts
processed_english = preprocess_multilang_text(ocr_text_english)
processed_tamil = preprocess_multilang_text(ocr_text_tamil)
processed_hindi = preprocess_multilang_text(ocr_text_hindi)

print("Processed English:", processed_english)
print("Processed Tamil:", processed_tamil)
print("Processed Hindi:", processed_hindi)