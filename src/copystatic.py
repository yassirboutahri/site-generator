import os 
import shutil

def copy_files_recursive(src_dir_path:str, dest_dir_path:str) -> None:
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for f in os.listdir(src_dir_path):
        from_path = os.path.join(src_dir_path, f)
        dest_path = os.path.join(dest_dir_path, f)

        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

    