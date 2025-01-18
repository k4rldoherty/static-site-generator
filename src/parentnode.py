from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:  
            raise ValueError("ParentNode must have at least one child")
        
        result = f"<{self.tag}>"

        for child in self.children:
            result += child.to_html()
        
        result += f"</{self.tag}>"

        return result