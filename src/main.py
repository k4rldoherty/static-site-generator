from src.textnode import TextNode, TextType
from src.utils import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    print(node)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

main()