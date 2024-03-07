from textnode import TextNode
from leafnode import LeafNode

def main():
    node = TextNode("This is text with a `code block` word", "text")
    print(node)

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

main()