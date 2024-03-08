import os
import shutil
from pathlib import Path
from block_markdown import markdown_to_html_node

def main():
    copy_from_directory("./static", "./public")
    generate_page_recursive("./content", "./template.html", "./public")

def copy_from_directory(src_path, dst_path, is_root = True):
    if not os.path.exists(src_path):
        raise Exception("The directory to copy does not exist")
    if is_root:
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        os.mkdir(dst_path)
    for child in os.listdir(src_path):
        src_child_path = os.path.join(src_path, child)
        dst_child_path = os.path.join(dst_path, child)
        print(f"{src_child_path} ---> {dst_child_path}")
        if os.path.isfile(src_child_path):
            shutil.copy(src_child_path, dst_child_path)
        else:
            if not os.path.exists(dst_child_path):
                os.mkdir(dst_child_path)
            copy_from_directory(src_child_path, dst_child_path, False)

def extract_title(markdown):
    # Title should always be an h1 at the start of the file
    if markdown == None or not isinstance(markdown, str):
        raise Exception("Markdown page does not exist or is in an invalid format")
    if not markdown.startswith("# "):
        raise Exception("Markdown page does not have a title (h1)")
    title = markdown.split("\n", 1)[0]
    return title.lstrip("# ")

def generate_page(src_path, template_path, dst_path):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}")
    src_content = read_file_content(src_path)
    tmp_content = read_file_content(template_path)
    src_title = extract_title(src_content)
    src_body = markdown_to_html_node(src_content).to_html()
    tmp_content = tmp_content.replace("{{ Title }}", src_title)
    tmp_content = tmp_content.replace("{{ Content }}", src_body)
    if not os.path.exists(os.path.dirname(dst_path)):
        os.makedirs(os.path.dirname(dst_path))
    if os.path.exists(dst_path):
        os.remove(dst_path)
    with open(dst_path, "w") as file:
        file.write(tmp_content)
    
def read_file_content(path):
    try:
        file = open(path, "r")
        content = file.read()
        file.close()
        return content
    except:
        print("I/O exception occurred")
        return None

def generate_page_recursive(src_path, template_path, dst_path):
    if not os.path.exists(src_path):
        raise Exception("The directory to copy does not exist")
    if os.path.isfile(src_path):
        file_name = Path(src_path).name.split(".")[0]
        generate_page(src_path, template_path, os.path.dirname(dst_path) + f"/{file_name}.html")
    else:
        for child in os.listdir(src_path):
            src_child_path = os.path.join(src_path, child)
            dst_child_path = os.path.join(dst_path, child)
            generate_page_recursive(src_child_path, template_path, dst_child_path)

main()