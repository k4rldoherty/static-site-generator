from src.page_generation import generate_page
from src.utils import copy_files, clean_public_folder
import os

def main():
    static_path = os.path.abspath("static")
    pub_path = os.path.abspath("public")
    clean_public_folder()
    copy_files(static_path, pub_path)
    from_path = os.path.abspath("content/index.md")
    template_path = os.path.abspath("template.html")
    dest_path = os.path.abspath("public")
    generate_page(from_path, template_path, dest_path)


main()