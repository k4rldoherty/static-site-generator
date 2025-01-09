from src.leafnode import LeafNode
from src.textnode import TextType, TextNode
import re


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
        # print(sections)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        # print(split_nodes)
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # only TextNodes are processed
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        # returns a list of tuples containing the link and description
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            # if no links are found, the original node is returned
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            # if there is any text before the link, it is added as a text node
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # a new text node for the link
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT, )]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
        
