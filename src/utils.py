import os
import shutil

def clean_public_folder():
    project_root = os.path.abspath(".")
    # Make sure both the source and destination are present
    if not os.path.exists("public"):
        return ValueError("Path to folder does not exist")
    # delete all files from destination
    public_dir = os.path.join(project_root, "public")
    ls_dest = os.listdir(public_dir)
    for item in ls_dest:
        item_path = os.path.join(public_dir, item)
        if os.path.isfile(os.path.join(public_dir, item)):
            os.remove(item_path)
            print(f"{item_path} is a file and it is gone!")
        elif os.path.isdir(os.path.join(public_dir, item)):
            print(f"{item_path} is a directory and it is gone!")
            shutil.rmtree(item_path)
    
def copy_files(source, destination):
    print("Copying files from the source to the destination folder . . .")
    source_dir = os.path.abspath(source)
    dest_dir = os.path.abspath(destination)

    to_copy = os.listdir(source_dir)
    print(f"{len(to_copy)} items found, copying . . .")
    for item in to_copy:
        if os.path.isfile(os.path.join(source_dir, item)):
            shutil.copy(os.path.join(source_dir, item), dest_dir)
            print(f"successfully copied {item}")
        if os.path.isdir(os.path.join(source_dir, item)):
            print(f"{item} is a directory, creating a new directory in destination to hold files . . .")
            # make a folder to store the 
            os.makedirs(os.path.join(dest_dir, item), exist_ok=True)
            # recursively call copy_files
            copy_files(os.path.join(source_dir, item), os.path.join(dest_dir, item))