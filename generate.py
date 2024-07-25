import argparse
import logging
import os
from generation.json_processor import process_json
from generation.js_creator import create_js
from generation.readme_updater import update_readme
from generation.json_sorter import sort_json

def setup_logging(debug_mode):
    if debug_mode:
        logging.basicConfig(
            filename='debug.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    else:
        logging.basicConfig(
            level=logging.CRITICAL,  # Suppress non-critical logs
        )

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process and convert JSON data.')
    parser.add_argument('--debug', action='store_true', help='Write debug information to a log file')
    args = parser.parse_args()

    setup_logging(args.debug)

    json_file = 'generation/comments_contrib.json'
    js_file = 'comments.js'
    markdown_file = 'generation/comments_contrib.md'
    readme_file = 'README.md'

    # Ask user whether to sort JSON
    while True:
        answer = input("Do you want to sort the JSON data alphabetically by 'name' before conversion? (Y/N): ").strip().upper()
        if answer in ['Y', 'N']:
            break
        print("Please enter 'Y' or 'N'.")

    if answer == 'Y':
        sort_json(json_file)

    if args.debug:
        # Log raw JSON data
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
        logging.debug("Raw JSON data:\n%s", json_data[:500])  # Log only the first 500 characters for brevity

    process_json(json_file, markdown_file)

    if args.debug:
        logging.debug("Markdown file '%s' created successfully.", markdown_file)

    create_js(json_file, js_file)

    print("\033[92mConversion successful!\033[0m")  # Green success message

    # Ask user whether to update README
    while True:
        answer = input("Do you want to update the README.md with the new content? (Y/N): ").strip().upper()
        if answer in ['Y', 'N']:
            break
        print("Please enter 'Y' or 'N'.")

    if answer == 'Y':
        update_readme(markdown_file, readme_file)
        print("\033[92mREADME.md updated successfully!\033[0m")  # Green success message
    else:
        print("\033[94mNo changes made to README.md.\033[0m.")

    # Remove markdown file
    if os.path.exists(markdown_file):
        os.remove(markdown_file)
        if args.debug:
            logging.debug("Removed markdown file '%s'.", markdown_file)
    else:
        if args.debug:
            logging.debug("Markdown file '%s' does not exist.", markdown_file)

if __name__ == "__main__":
    main()
