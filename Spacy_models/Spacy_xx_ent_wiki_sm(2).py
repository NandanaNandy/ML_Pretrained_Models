import re
import spacy
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
import pytz
import tracemalloc
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PerformanceDocumentExtractor:
    def __init__(self, model_name: str = 'xx_ent_wiki_sm', enable_memory_profiling: bool = False):
        """
        Initialize the extractor with the SpaCy model and optional memory profiling.
        """
        try:
            self.nlp = spacy.load(model_name)
            logging.info(f"SpaCy model '{model_name}' loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load SpaCy model: {e}")
            raise

        self.enable_memory_profiling = enable_memory_profiling

        # Extraction patterns
        self.extraction_patterns = {
            'name_patterns': [
                r'(?:Selvan|Thiru)\s+([A-Za-z\s]+)',
                r'Name\s*:?\s*([A-Za-z\s]+)',
                r'([A-Za-z\s]+)\s+(?:son|daughter)\s+of'
            ],
            'parent_patterns': [
                r'(?:son|daughter)\s+of\s+(Thiru\s+[A-Za-z\s]+)',
                r'Father\'s\s+Name\s*:?\s*([A-Za-z\s]+)',
                r'Parent\s*:?\s*([A-Za-z\s]+)'
            ],
            'address_patterns': [
                r'Door\s*(?:No)?\s*:?\s*(\d+/?\d*),?\s*([A-Za-z\s]+)\s+(?:of|in)\s+([A-Za-z\s]+)\s+(?:Village|Town|District)',
                r'Address\s*:?\s*([^\n]+)'
            ]
        }
    
    def extract_entities_with_timing(self, text: str) -> Dict[str, Any]:
        """
        Extract entities with detailed timing and performance metrics
        """
        performance_metrics = {
            'total_extraction_time': 0,
            'method_timings': {}
        }

        total_start_time = time.time()
        if self.enable_memory_profiling:
            tracemalloc.start()

        entities = {}

        def timed_extraction(method, *args):
            start_time = time.time()
            start_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

            result = method(*args)

            end_time = time.time()
            end_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

            method_name = method.__name__
            performance_metrics['method_timings'][method_name] = {
                'execution_time': end_time - start_time,
                'memory_used': (end_memory - start_memory) if start_memory is not None else 'Not tracked'
            }

            return result

        entities['name'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['name_patterns'])
        entities['parent_name'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['parent_patterns'])
        entities['address'] = timed_extraction(self.extract_by_patterns, text, self.extraction_patterns['address_patterns'])

        spacy_start_time = time.time()
        spacy_start_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

        doc = self.nlp(text)
        spacy_entities = [
            {
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            } for ent in doc.ents
        ]

        spacy_end_time = time.time()
        spacy_end_memory = tracemalloc.get_traced_memory()[0] if self.enable_memory_profiling else None

        performance_metrics['method_timings']['spacy_ner'] = {
            'execution_time': spacy_end_time - spacy_start_time,
            'memory_used': (spacy_end_memory - spacy_start_memory) if spacy_start_memory is not None else 'Not tracked'
        }

        total_end_time = time.time()
        performance_metrics['total_extraction_time'] = total_end_time - total_start_time

        if self.enable_memory_profiling:
            tracemalloc.stop()

        return {
            'extracted_entities': entities,
            'spacy_entities': spacy_entities,
            'performance_metrics': performance_metrics
        }
    
    def extract_by_patterns(self, text: str, pattern_list: List[str]) -> Optional[str]:
        """
        Dynamically extract information using multiple regex patterns
        """
        for pattern in pattern_list:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

def main():
    sample_texts = [
        "This is to certify that Selvan Nareshkanna $ son of Thiru Shanmugam residing at Door No 164/5, Periyar nagar of Harur Village / Town Harur Taluk Dharmapuri District of the State of Tamil Nadu belongs to 24 Manai Telugu Chetty Community, which is recognized as a Backward Class as per Government Order (Ms) No. 85, Backward Classes Most Backward Classes and Minority Welfare Department (BCC), dated 2gth July 2008 vide Serial No 100 Signature Not Verifie GDigitally Signed oB P6:ZANSSAMY Date: 08:26:26 IST",
        "Certificate of Identification: Name: John Doe, son of Robert Doe, residing at 123 Main Street, Springfield Town. Community: 10 Manai Regional Group. Government Order No. 42, Welfare Department, dated 15th August 2020. Digitally Signed: X9Y2Z1 on 10:30:45 IST"
    ]

    extractor = PerformanceDocumentExtractor(enable_memory_profiling=True)

    for i, text in enumerate(sample_texts, 1):
        print(f"\n{'='*50}")
        print(f"DOCUMENT {i} ENTITY EXTRACTION PERFORMANCE")
        print(f"{'='*50}")
        results = extractor.extract_entities_with_timing(text)

        print("\n[1] EXTRACTED ENTITIES:")
        print(json.dumps(results['extracted_entities'], indent=2))

        print("\n[2] SPACY ENTITIES:")
        print(json.dumps(results['spacy_entities'], indent=2))

        print("\n[3] PERFORMANCE METRICS:")
        perf_metrics = results['performance_metrics']
        print(f"Total Extraction Time: {perf_metrics['total_extraction_time']:.6f} seconds")
        print("\nMethod-wise Timings:")
        for method, metrics in perf_metrics['method_timings'].items():
            print(f"- {method}:")
            print(f"  Execution Time: {metrics['execution_time']:.6f} seconds")
            print(f"  Memory Used: {metrics['memory_used']} bytes")

if __name__ == '__main__':
    main()
