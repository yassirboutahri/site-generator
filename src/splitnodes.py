from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type:TextType) -> list[TextNode]:
    if not delimiter:
        raise Exception("invalid markdownd syntex delimiter") 

    if delimiter == "`":
        t_type = TextType.CODE
    elif delimiter == "**":
        t_type = TextType.BOLD
    elif delimiter == "_":
        t_type = TextType.ITALIC

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        
        splited_old_node = old_node.text.split(delimiter)
        new_nodes.append(TextNode(splited_old_node[0], old_node.text_type))
        new_nodes.append(TextNode(splited_old_node[1], t_type))
        new_nodes.append(TextNode(splited_old_node[2], old_node.text_type))

    return new_nodes
