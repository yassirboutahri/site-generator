from enum import Enum
from htmlnode import ParentNode, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_blocks(markdown:str):
    blocks = markdown.split("\n\n")
    splite_blocks= []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        splite_blocks.append(block)
    return splite_blocks 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown:str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    childrens = []
    for block in blocks:
        html_node = block_to_html_node(block)
        childrens.append(html_node)
    return ParentNode("div", childrens, None)

def block_to_html_node(block:str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text:str) -> list[HTMLNode]:
    text_nodes= text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children 

def paragraph_to_html_node(block:str) -> ParentNode:
    lines = block.split("\n")
    text = " ".join(lines)
    childrens = text_to_children(text)
    return ParentNode("p", childrens)

def heading_to_html_node(block:str) -> ParentNode:
    level = 0
    for chart in block:
        if chart != "#":
            break
        level +=1
    if level +1 >=len(block):
        raise ValueError(f"invlid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block:str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def olist_to_html_node(block:str) -> ParentNode:
    lines = block.split("\n")
    html_items = []
    for line in lines:
        parts = line.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block: str):
    lines = block.split("\n")
    html_nodes = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_nodes.append(ParentNode("li", children))
    return ParentNode("ul", html_nodes)

def quote_to_html_node(block:str):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
        
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

     
        
         