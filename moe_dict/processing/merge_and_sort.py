import json
from tqdm import tqdm

def merge_and_filter_json(file1, file2, output_file):
    # Load both JSON files
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    # Combine the data
    combined_data = data1 + data2
    print(f"Total entries after merging: {len(combined_data)}")

    # Sort by dict_id
    combined_data.sort(key=lambda x: x['dict_id'])
    
    # Track seen hak_ex entries and filter duplicates
    unique_entries = []
    seen_hak_ex = set()
    duplicates = []

    for entry in tqdm(combined_data, desc="Filtering duplicates"):
        hak_ex = entry["hak_ex"]
        
        # If hak_ex is already seen, consider it a duplicate
        if hak_ex in seen_hak_ex:
            duplicates.append(entry)  # Store duplicates for printing
        else:
            seen_hak_ex.add(hak_ex)
            unique_entries.append(entry)

    # Print the number of unique entries and duplicates
    print(f"Unique entries: {len(unique_entries)}")
    print(f"Duplicate entries: {len(duplicates)}")

    # Print duplicates
    print("Duplicate entries based on hak_ex:")
    for duplicate in duplicates:
        print(duplicate)

    # Save the unique sorted entries to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_entries, f, ensure_ascii=False, indent=2)

# Define file paths
file1 = "filtered_example_sentences.json"
file2 = "processed_problematic_sentences.json"
output_file = "merged_unique_sentences.json"

# Run the merging and filtering function
merge_and_filter_json(file1, file2, output_file)
