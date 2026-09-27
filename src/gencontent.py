from block_markdown import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path) as file:
        from_path_content = file.read()
    with open(template_path) as file:
        template_path_content = file.read()
    html_string = markdown_to_html_node(from_path_content).to_html()   
    title = extract_title(from_path_content)

    template_path_content = template_path_content.replace("{{ Title }}", title)
    template_path_content = template_path_content.replace("{{ Content }}", html_string)

    dest_dir_path = os.path.dirname(dest_path)    
    if dest_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)    
    with open(dest_path, "w") as file:
        file.write(template_path_content)
        

def extract_title(markdown:str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("invalid h1")