from src.textnode import TextNode, TextType
from src.block import markdown_to_blocks

def main():
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

    l = markdown_to_blocks(markdown)
    print(l)
    for x in l:
        print(x)
        print("\n")

main()