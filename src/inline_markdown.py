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
