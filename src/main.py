import os
import shutil
from textnode import TextNode

def main():
    
    copy_from_directory("./static", "./public")

def copy_from_directory(root_dir, target_root_dir, is_root = True):
    if not os.path.exists(root_dir):
        raise Exception("The directory to copy does not exist")
    if is_root:
        if os.path.exists(target_root_dir):
            shutil.rmtree(target_root_dir)
        os.mkdir(target_root_dir)
    for child in os.listdir(root_dir):
        src_path = os.path.join(root_dir, child)
        dst_path = os.path.join(target_root_dir, child)
        print(f"{src_path} ---> {dst_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            copy_from_directory(src_path, dst_path, False)


main()