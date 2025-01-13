from src.textnode import TextNode, TextType
from src.block import block_to_block_type

def main():

    h = "###  "
    h1 = "### h3"
    print(block_to_block_type(h))
    print(block_to_block_type(h1))

main()