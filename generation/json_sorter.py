import json
import logging

def sort_json(json_file):
    # Read JSON file with UTF-8 encoding
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    logging.debug("Raw JSON data before sorting:\n%s", json.dumps(data, indent=4))  # Log before sorting
    
    # Sort JSON data by 'name' field
    sorted_data = sorted(data, key=lambda x: x.get('name', ''))

    # Write sorted JSON data back to the original file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=4)

    print(f"JSON file '{json_file}' sorted successfully.")
