class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return None
        
        prop_str = ""
        for prop in self.props.items():
            prop_str += f' {prop[0]}="{prop[1]}"'
        return prop_str

    def __eq__(self, htmlnode):
        if not isinstance(htmlnode, HTMLNode):
            return False
        return (
            self.tag == htmlnode.tag and
            self.value == htmlnode.value and
            self.children == htmlnode.children and
            self.props == htmlnode.props
        )

    def __repr__(self):
        repr_str = ""
        for item in self.__dict__.items():
            repr_str += f"{item[0]}: {item[1]}\n"
        return repr_str

class ParentNode(HTMLNode):

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node tag cannot be None")
        html_str = f"<{self.tag}{self.props_to_html() if self.props != None else ''}>{self.value if self.value != None else ""}"

        if self.children != None:
            for child in self.children:
                html_str += child.to_html()

        return html_str + f"</{self.tag}>"

class LeafNode(HTMLNode):

    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html() if self.props != None else ""}>{self.value if self.value != None else ""}</{self.tag}>"