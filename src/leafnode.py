from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None ):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )

    def to_html(self):
        if self.tag is None:
            return str(self.value)
    
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"