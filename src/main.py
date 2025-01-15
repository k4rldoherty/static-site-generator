from src.textnode import TextNode, TextType
from src.block import markdown_to_html_node, block_to_block_type

def main():
    p = """> quote line 1
> quote line 2"""

    print(markdown_to_html_node(p))

main()