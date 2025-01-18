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
    md_file = open(from_path, 'r')
    md_string = md_file.read()
    template_file = open(template_path, 'r')
    template_string = template_file.read()
    md_html_string = markdown_to_html_node(md_string)
    title = extract_title(md_string)
    template_with_content = template_string.replace("{{ Content }}", md_html_string)
    completed_template = template_with_content.replace("{{ Title }}", title)
    print("Finished generating html.")
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
