from src.page_generation import generate_pages_recursive
from src.utils import copy_files, clean_public_folder
import os

def main():
    static_path = os.path.abspath("static")
    pub_path = os.path.abspath("public")
    clean_public_folder()
    copy_files(static_path, pub_path)
    from_path = os.path.abspath("content")
    template_path = os.path.abspath("template.html")
    generate_pages_recursive(from_path, template_path, pub_path)


main()