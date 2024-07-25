import logging

def create_js(json_file, js_file):
    # Read JSON file with UTF-8 encoding
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = file.read()
    
    logging.debug("Raw JSON data for JS conversion:\n%s", json_data[:500])  # Log only the first 500 characters for brevity

    # Encapsulate JSON data in callback[()]
    js_content = f"callback[\n(\n{json_data}\n)\n]"

    # Write to JS file with UTF-8 encoding
    with open(js_file, 'w', encoding='utf-8') as file:
        file.write(js_content)
    logging.info("JS file '%s' created successfully.", js_file)
