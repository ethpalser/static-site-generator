from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if not isinstance(text_node, TextNode):
            return False
        return (
            self.text == text_node.text and
            self.text_type == text_node.text_type and
            self.url == text_node.url
        )
    
    def __repr__(self):
        return f"text: {self.text}, text_type: {self.text_type}, url: {self.url}"
    

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