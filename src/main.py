from src.textnode import TextNode, TextType
from src.block import markdown_to_html_node

def main():
    md = """# Header

paragraph

- list item 1
- list item 2

[link](www.google.com)

![alt text](some text)

__italics__

**bold**
"""
    print(markdown_to_html_node(md))

main()