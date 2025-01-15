from src.utils import clean_public_folder, copy_files

def main():
    clean_public_folder()
    copy_files("static", "public")

main()