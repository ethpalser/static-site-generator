from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html() if self.props != None else ""}>{self.value}</{self.tag}>"