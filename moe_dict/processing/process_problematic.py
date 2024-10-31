import json
from tqdm import tqdm
import re

def process_sentences(input_file, output_file):
    # Load the JSON data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_entries = []

    # Process each entry in the JSON
    for entry in tqdm(data, desc="Processing entries"):
        dict_id = entry["dict_id"]
        hak_ex = entry["hak_ex"]
        zh_ex = entry["zh_ex"]

        # Split hak_ex by '、' and check for parentheses
        hak_phrases = re.split(r'、', hak_ex)
        zh_default = zh_ex if '、' not in zh_ex else zh_ex.split('、')[-1]

        # Iterate through hak_phrases, keeping only items with matching parentheses or the last item
        for i, hak_phrase in enumerate(hak_phrases):
            match = re.search(r'（(.*?)）', hak_phrase)
            
            # Include only phrases with parentheses or the last phrase without parentheses
            if match or i == len(hak_phrases) - 1:
                hak_phrase_cleaned = re.sub(r'（.*?）', '', hak_phrase)
                zh_translation = match.group(1) if match else zh_default
                processed_entries.append({
                    "dict_id": dict_id,
                    "hak_ex": hak_phrase_cleaned,
                    "zh_ex": zh_translation
                })

    # Save the processed entries to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_entries, f, ensure_ascii=False, indent=2)

# Define input and output files
input_file = "problematic_sentences_1.json"
output_file = "processed_problematic_sentences_1.json"

# Run the processing function
process_sentences(input_file, output_file)
