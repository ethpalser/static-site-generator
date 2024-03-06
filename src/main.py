from textnode import TextNode
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def main():
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Cannot convert a value that is not a Text Node to HTML Node")

    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode(None, "", {
            "src": text_node.url,
            "alt": text_node.text
        })
    raise ValueError("Text Node not a valid type to convert into HTML Node")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes == None:
        raise ValueError("Cannot split None")
    if delimiter == None:
        return old_nodes

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue

        nodes_split = node.text.split(delimiter)
        if len(nodes_split) % 2 == 0:
            raise Exception(f"Invalid markdown text format for the delimiter: {delimiter}")

        for i in range(0, len(nodes_split)):
            if i % 2 != 0:
                new_nodes.append(TextNode(nodes_split[i], text_type))
            else:
                new_nodes.append(TextNode(nodes_split[i], node.text_type))
    return new_nodes

main()