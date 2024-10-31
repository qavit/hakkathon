import json
from tqdm import tqdm

def load_and_merge_json(file1, file2, output_file):
    # Load data from both JSON files
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    
    # Merge data and sort by `dict_id`
    combined_data = data1 + data2
    combined_data.sort(key=lambda x: x["dict_id"])
    
    # Remove duplicates and store repeated entries
    unique_entries = []
    duplicates = []
    seen_entries = set()  # Using set to track unique (hak_ex, zh_ex) pairs

    for entry in tqdm(combined_data, desc="Processing entries"):
        entry_pair = (entry["hak_ex"], entry["zh_ex"])
        if entry_pair in seen_entries:
            duplicates.append(entry)  # Log duplicate entry
        else:
            seen_entries.add(entry_pair)
            unique_entries.append(entry)

    # Output duplicates
    print("Duplicate entries found:")
    for duplicate in duplicates:
        print(duplicate)

    # Save the unique entries to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_entries, f, ensure_ascii=False, indent=2)

# Define input and output files
file1 = "filtered_example_sentences_1.json"
file2 = "processed_problematic_sentences_1.json"
output_file = "merged_sorted_unique_sentences.json"

# Run the function
load_and_merge_json(file1, file2, output_file)
