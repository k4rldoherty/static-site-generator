from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    text_types = [item.value for item in TextType]
    if text_node.text_type not in text_types:
        raise Exception("Text type not found")
    else:
        if text_node.text_type == TextType.BOLD.value:
                return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.LINK.value:
            return LeafNode("a", text_node.text, props={'href': text_node.url})
        elif text_node.text_type == TextType.CODE.value:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.IMAGE.value:
                return LeafNode('img', "", {'src': text_node.url, 'alt': text_node.text})