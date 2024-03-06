class TextNode:

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return (
            self.text == text_node.text and
            self.text_type == text_node.text_type and
            self.url == text_node.url
        )
    
    def __repr__(self):
        return f"text: {self.text}, text_type: {self.text_type}, url: {self.url}"