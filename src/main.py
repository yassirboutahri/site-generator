import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontentrecursively import generate_pages_recursive

dir_path_static = "./static" 
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if not sys.argv[1]:
        basepath = sys.argv[1]
    else:
        basepath = "/"

        
    print("deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
        

    print("copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

    
main()
