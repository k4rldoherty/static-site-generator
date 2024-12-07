from leafnode import LeafNode
from textnode import TextType, TextNode


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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # if the old node is of type text, add it to the new nodes 
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        # split the old node by the delimiter
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


