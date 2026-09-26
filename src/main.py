import os
import shutil

from copystatic import copy_files_recursive
from gen import generate_page

dir_path_static = "./static" 
dir_path_public = "./public"

def extract_title(markdown:str):
    lines = markdown.split("\n")
    if not markdown.startswith("# "):
        raise ValueError("invalid h1")

    return lines[0][2:].strip()


def main():
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")

    
main()
