from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node tag cannot be None")
        html_str = f"<{self.tag}{self.props_to_html() if self.props != None else ''}>{self.value}"

        if self.children != None:
            for child in self.children:
                html_str += child.to_html()

        return html_str + f"</{self.tag}>"
