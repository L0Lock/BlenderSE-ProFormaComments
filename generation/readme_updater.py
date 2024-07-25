def update_readme(markdown_file, readme_file):
    # Read markdown content with UTF-8 encoding
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Read README and update content with UTF-8 encoding
    with open(readme_file, 'r', encoding='utf-8') as file:
        readme_lines = file.readlines()

    # Find the line with `## Content:`
    for i, line in enumerate(readme_lines):
        if line.startswith("## Content:"):
            # Replace content after this line
            readme_lines = readme_lines[:i+1]
            readme_lines.append(markdown_content)
            break
    else:
        # If `## Content:` not found, append it
        readme_lines.append("\n## Content:\n")
        readme_lines.append(markdown_content)

    # Write back to README with UTF-8 encoding
    with open(readme_file, 'w', encoding='utf-8') as file:
        file.writelines(readme_lines)
