import time
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langdetect import detect

# Load pre-trained translation model
try:
    translation_model_name = "Helsinki-NLP/opus-mt-mul-en"
    translation_tokenizer = AutoTokenizer.from_pretrained(translation_model_name)
    translation_model = AutoModelForSeq2SeqLM.from_pretrained(translation_model_name)
    print("Translation model loaded successfully.")
except Exception as e:
    print(f"Error loading translation model: {e}")

# Load NER pipeline
try:
    ner_model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
    ner_pipeline = pipeline("ner", model=ner_model_name, aggregation_strategy="simple")
    print("NER model loaded successfully.")
except Exception as e:
    print(f"Error loading NER model: {e}")

# Translate text to English
def translate_to_english(text):
    try:
        start_time = time.time()
        inputs = translation_tokenizer.encode(text, return_tensors="pt", truncation=True)
        outputs = translation_model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        translated_text = translation_tokenizer.decode(outputs[0], skip_special_tokens=True)
        duration = time.time() - start_time
        print(f"Translation Time: {duration:.4f} seconds")
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""

# Extract entities from text
def extract_entities(text):
    try:
        start_time = time.time()
        entities = ner_pipeline(text)
        duration = time.time() - start_time
        print(f"NER Time: {duration:.4f} seconds")
        # Simplify output
        return [{"word": ent["word"], "entity": ent["entity_group"]} for ent in entities]
    except Exception as e:
        print(f"Error during NER: {e}")
        return []

# Detect the language of the input text
def detect_language(text):
    try:
        start_time = time.time()
        language = detect(text)
        duration = time.time() - start_time
        print(f"Language Detection Time: {duration:.4f} seconds")
        return language
    except Exception as e:
        print(f"Error during language detection: {e}")
        return "unknown"

# Complete pipeline: Translation + NER
def process_multilingual_text(text):
    try:
        print(f"Processing text: {text}")
        start_time = time.time()
        
        # Detect language
        detected_language = detect_language(text)
        print(f"Detected Language: {detected_language}")
        
        # Translate to English
        translated_text = translate_to_english(text)
        
        # Perform NER
        entities = extract_entities(translated_text)
        
        total_duration = time.time() - start_time
        print(f"Total Processing Time: {total_duration:.4f} seconds")
        
        return {
            "original_text": text,
            "translated_text": translated_text,
            "entities": entities
        }
    except Exception as e:
        print(f"Error during processing: {e}")
        return {}

# Sample input texts in different languages
texts = [
    """Serial Mo GOVERNMENT OF TAMIL NADU CMA DEPARTMENT QF TECHNICAL EDUCAION 044493 CONSOLIDATED MARKSHEET Kom Date of Birth Name 0f Student Register Number 30-Jun-1988 RAMESH P N 2413465 Name & Address of the Institution Institution Code KS RENGASAMY INSTITUTE OF TECHNOLOGY 328 GOUNDAMPALAYAM THOKAVADI PO 637 209 Discipline Scheme ELECTRICAL AND ELECTRONICS ENGINEERING (FULL TIME) J SCHEME 1030 Minimum Marks Month & Year of Maximum Marks Year/ Column Subject Name Marks for Pass Secured Passing Semester Number 100 40 50 APR 2004 01 ENGLISH 100 40 59 APR 2004 02* BASICS OF COMPUTER SCIENCE 100 40 74 APR 2004 03* MATHEMATICS 100 40 82 APR 2004 04* MATHEMATICS II 100 40 70 APR 2004 05* APPLIED PHYSICS 100 40 81 APR 2004 06* APPLIED CHEMISTRY 100 40 58 APR 2004 07* TECHNICAL DRAWING 100 50 90 APR 2004 08* APPLIED PHYSICS PRACTICAL 100 50 67 APR 2004 09* APPLIED CHEMISTRY PRACTICAL 100 50 82 APR 2004 10* WORKSHOP 100 50 84 APR 2004 11 ENGLISH COMMUNICATION PRACTICAL 100 40 67 OCT 2004 01 ELECTRICAL CIRCUIT THEORY 100 40 63 OCT 2004 02 ELECTRICAL MACHINES 100 40 55 OCT 2004 03 ELECTRONIC DEVICES AND CIRCUITS 100 50 94 OCT 2004 04 ELECTRICAL MACHINES LAB 100 50 87 OCT 2004 05 ELECTRONIC DEVICES AND CIRCUITS LAB 100 50 94 OCT 2004 06 MS OFFICE LAB 100 40 73 APR 2005 01 ELECTRICAL MACHINES Il 100 40 75 APR 2005 02 MEASUREMENT AND INSTRUMENTATION 100 40 80 APR 2005 03 BASICS OF MECHANICAL ENGINEERING 100 50 89 APR 2005 04 ELECTRICAL MACHINES LAB II 50 90 APR 2005 05 COMPUTER AIDED ELECTRICAL DRAWING LAB 100 97 APR 2005 06 MECHANICAL ENGINEERING LAB 100 50 01 GENERATION TRANSMISSION AND SWITCHGEAR 100 40 92 OCT 2005 02 ANALOG AND DIGITAL ELECTRONICS 100 40 80 OCT 2005 03 ET1-CONTROL OF ELECTRICAL MACHINES 100 40 76 OCT 2005 04 WIRING WINDING AND ESTIMATION LAB 100 50 89 OCT 2005 05 ANALOG AND DIGITAL ELECTRONICS LAB 100 50 94 OCT 2005 06 EP-CONTROL OF ELECTRICAL MACHINES LAB 100 50 93 OCT 2005 01 DISTRIBUTION AND UTILISATION 100 40 82 APR 2006 02 MICRO CONTROLLERS 100 40 61 APR 2006 03 ET2-POWER ELECTRONICS 100 40 88 APR 2006 04 MICRO CONTROLLER LAB 100 50 90 APR 2006 05 EP-POWER ELECTRONICS LAB 100 50 96 APR 2006 06 PROJECT WORK AND ENTREPRENEURSHIP 100 50 97 APR 2006 DURATION OF THE COURSE THREE YEARS Diploma Certificate Total Marks Percentage Class Provisional Certificate Number Number 2002 / 2400 83.42 % FIRST CLASS WITH HONOURS ABO235447 B252706 Marks in these subject(s) are not included for computation of aggregate total and award of class 9176 DATE 07-SEP-2006 CHAIRMAN BOARD OF EXAMINATIONS, CHENNAI-25"""

]

# Process each text
for text in texts:
    result = process_multilingual_text(text)
    print("\nResults:")
    print(f"Original Text: {result.get('original_text')}")
    print(f"Translated Text: {result.get('translated_text')}")
    print(f"Entities: {result.get('entities')}")
    print("-" * 50)
