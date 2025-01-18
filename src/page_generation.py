from src.block import markdown_to_html_node
import os

def extract_title(markdown):
    md_split = markdown.split("\n")
    for line in md_split:
        if line.startswith("# "):
            return line.removeprefix("# ")
    raise ValueError("No heading has been found")

def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")
    # Read the markdown file at from_path and store the contents in a variable.
    md_file = open(from_path, 'r')
    md_string = md_file.read()
    # Read the template file at template_path and store the contents in a variable.
    template_file = open(template_path, 'r')
    template_string = template_file.read()
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    md_html_string = markdown_to_html_node(md_string)
    # Use the extract_title function to grab the title of the page.
    title = extract_title(md_string)
    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    template_with_content = template_string.replace("{{ Content }}", md_html_string)
    completed_template = template_with_content.replace("{{ Title }}", title)
    print("Finished generating html.")
    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    finished_file = open(f"{dest_path}/index.html", 'x')
    finished_file.write(completed_template)
    md_file.close()
    template_file.close()
    finished_file.close()

def generate_pages_recursive(from_path, template_path, dest_path):
    for item in os.listdir(from_path):
        path = os.path.join(from_path, item)
        if os.path.isfile(path):
            generate_page(path, template_path, dest_path)
        if os.path.isdir(path):
            os.makedirs(os.path.join(dest_path, item), exist_ok=True)
            generate_pages_recursive(path, template_path, os.path.join(dest_path, item))
