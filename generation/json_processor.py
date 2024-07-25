import json
import logging

def process_json(json_file, markdown_file):
    # Read JSON file with UTF-8 encoding
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = file.read()
    
    logging.debug("Raw JSON data for processing:\n%s", json_data[:500])  # Log only the first 500 characters for brevity

    # Parse JSON data
    try:
        data = json.loads(json_data)
        logging.debug("Parsed JSON data:\n%s", data[:5])  # Log first 5 items for brevity
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        return

    # Write to markdown file with UTF-8 encoding
    with open(markdown_file, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"### {item['name']}\n")
            file.write(f"{item['description']}\n\n")

    # logging.info("Markdown file '%s' created successfully.", markdown_file)
