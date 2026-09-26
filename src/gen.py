from block_markdown import markdown_to_html_node
import os

def extract_title(markdown:str):
    lines = markdown.split("\n")
    if not markdown.startswith("# "):
        raise ValueError("invalid h1")

    return lines[0][2:].strip()



def generate_page(from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_path_content = file.read()
    with open(template_path) as file:
        template_path_content = file.read()
    html_string = markdown_to_html_node(from_path_content).to_html()   
    title = extract_title(from_path_content)

    template_path_content = template_path_content.replace("{{ Title }}", title)
    template_path_content = template_path_content.replace("{{ Content }}", html_string)

    dest_split = dest_path.split("/")
    if not os.path.exists(dest_split[0]):
        os.makedirs("/".join(dest_split[0:-1]))

        
    with open(dest_path, "w") as file:
        file.write(template_path_content)
        

