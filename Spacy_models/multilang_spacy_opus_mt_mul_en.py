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
    "அவரின் பெயர் ஜான் டோ, பிறந்த தேதி 5 மார்ச் 1990.",  # Tamil
]

# Process each text
for text in texts:
    result = process_multilingual_text(text)
    print("\nResults:")
    print(f"Original Text: {result.get('original_text')}")
    print(f"Translated Text: {result.get('translated_text')}")
    print(f"Entities: {result.get('entities')}")
    print("-" * 50)
