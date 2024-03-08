import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes == None:
        return None
    if delimiter == None:
        return old_nodes

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        node_split = node.text.split(delimiter)
        if len(node_split) % 2 == 0:
            raise Exception(f"Invalid markdown text format for the delimiter: {delimiter}")
        for i in range(0, len(node_split)):
            if i % 2 != 0:
                new_nodes.append(TextNode(node_split[i], text_type))
            else:
                new_nodes.append(TextNode(node_split[i], node.text_type))
    return new_nodes

def extract_markdown_images(text):
    if text == None:
        return []
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    if text == None:
        return []
    return re.findall(r"(?:(?<!!))\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    if old_nodes == None:
        return None
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            node_split = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
            for match in images:
                node_split.remove(match[0])
                node_split.remove(match[1])
            img_pos = 0
            for i in range(0, len(node_split)):
                if node_split[i] != "":
                    new_nodes.append(TextNode(node_split[i], text_type_text))
                if i % 2 == 0:
                    new_nodes.append(TextNode(images[img_pos][0], text_type_image, images[img_pos][1]))
                    img_pos += 1
    return new_nodes


def split_nodes_link(old_nodes):
    if old_nodes == None:
        return None
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            node_split = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
            for match in links:
                node_split.remove(match[0])
                node_split.remove(match[1])
            link_pos = 0
            for i in range(0, len(node_split)):
                if node_split[i] != "":
                    new_nodes.append(TextNode(node_split[i], text_type_text))
                if i % 2 == 0:
                    new_nodes.append(TextNode(links[link_pos][0], text_type_link, links[link_pos][1]))
                    link_pos += 1
    return new_nodes

def text_to_textnodes(text):
    if not isinstance(text, str) and not isinstance(text, TextNode):
        raise ValueError(f"Converting values of {text.__class__} to textnodes is not supported")
    to_convert = [text] if isinstance(text, TextNode) else [TextNode(text, text_type_text)]
    return(split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(to_convert, "**", text_type_bold), "*", text_type_italic), "`", text_type_code))))