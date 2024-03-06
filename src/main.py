from textnode import TextNode
from leafnode import LeafNode

def main():
    node = TextNode("The World", "bold", "https://google.com")
    print(node)

def text_node_to_html_node(text_node):
    if text_node is not TextNode:
        raise ValueError("Cannot convert a value that is not a Text Node to HTML Node")

    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(None, "", {
            "src": text_node.url,
            "alt": text_node.text
        })
    raise ValueError("Text Node not a valid type to convert into HTML Node")

main()