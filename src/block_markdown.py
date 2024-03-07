import re
from parentnode import ParentNode
from leafnode import LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    if not isinstance(markdown, str):
        raise Exception("Cannot convert non-string text into blocks")
    return markdown.split("\n\n")

def block_to_block_type(block):
    if re.search(r"^[#]{1,6}\s{1}.*", block) is not None:
        return block_type_heading
    elif re.search(r"^```[\w\s]*```$", block) is not None:
        return block_type_code
    elif re.search(r"^\>\s.*", block) is not None:
        lines = block.split("\n")
        for line in lines:
            if re.search(r"^>\s.*", line) is None:
                return block_type_paragraph
        return block_type_quote
    elif re.search(r"^[*-]\s.*", block) is not None:
        lines = block.split("\n")
        for line in lines:
            if re.search(r"^[*-]\s.*", line) is None:
                return block_type_paragraph
        return block_type_unordered_list
    elif re.search(r"^[0-9]\.\s.*", block) is not None:
        lines = block.split("\n")
        num = 1
        for line in lines:
            if re.search(r"^[0-9]\.\s.*", line) is None or line[:len(f"{num}")] != f"{num}":
                return block_type_paragraph
            num += 1
        return block_type_ordered_list
    return block_type_paragraph

# block_to_html_node

def block_to_heading_html_node(block):
    if block_to_block_type(block) != block_type_heading:
        raise ValueError("Cannot convert non-heading block into a heading node")
    heading_count = 0
    for i in range(0, len(block)):
        if block[i] != "#":
            break
        heading_count += 1
    return ParentNode(f"h{heading_count}", None, list(map(text_node_to_html_node, text_to_textnodes(block[heading_count + 1:]))))
    
def block_to_code_html_node(block):
    if block_to_block_type(block) != block_type_code:
        raise ValueError("Cannot convert non-code block into a code node")
    return ParentNode("pre", None, [LeafNode("code", block[3:-3])])

def block_to_quote_html_node(block):
    if block_to_block_type(block) != block_type_quote:
        raise ValueError("Cannot convert non-quote block into a quote node")
    value = "\n".join(map(lambda str : str[2:], block.split("\n")))
    return ParentNode("blockquote", None, list(map(text_node_to_html_node, text_to_textnodes(value))))

def block_to_unordered_list_html_node(block):
    if block_to_block_type(block) != block_type_unordered_list:
        raise ValueError("Cannot convert non-unordered-list block into a unordered list node")
    list_nodes = []
    items = map(lambda str : str[2:], block.split("\n"))
    for item in items:
        list_nodes.append(ParentNode("li", None, list(map(text_node_to_html_node, text_to_textnodes(item)))))
    return ParentNode("ul", None, list_nodes)

def block_to_ordered_list_html_node(block):
    if block_to_block_type(block) != block_type_ordered_list:
        raise ValueError("Cannot convert non-ordered-list block into a ordered list node")
    list_nodes = []
    items = block.split("\n")
    for i in range(0, len(items)):
        list_nodes.append(ParentNode("li", None, list(map(text_node_to_html_node, text_to_textnodes(items[i][3 + i//10:])))))
    return ParentNode("ol", None, list_nodes)

def block_to_paragraph_html_node(block):
    if block_to_block_type(block) != block_type_paragraph:
        raise ValueError("Cannot convert non-paragraph block into a paragraph node")
    return ParentNode("p", None, list(map(text_node_to_html_node, text_to_textnodes(block))))

# markdown_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            nodes.append(block_to_heading_html_node(block))
        elif block_type == block_type_code:
            nodes.append(block_to_code_html_node(block))
        elif block_type == block_type_quote:
            nodes.append(block_to_quote_html_node(block))
        elif block_type == block_type_unordered_list:
            nodes.append(block_to_unordered_list_html_node(block))
        elif block_type == block_type_ordered_list:
            nodes.append(block_to_ordered_list_html_node(block))
        else:
            nodes.append(block_to_paragraph_html_node(block))
    return ParentNode("div", None, nodes)