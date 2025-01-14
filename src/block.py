from src.block_utils import check_header, check_ordered_list, check_quote, check_unordered_list

def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for element in markdown_split:
        element = element.strip()
        if element:
            blocks.append(element)

    
    return blocks

def block_to_block_type(block):
    # takes in a single block of markdown, and returns a string representing what type the block is.
    # Heading
    if block[0] == "#":
        check = check_header(block)
        if check != -1: return check
    # Code
    if block.startswith("``` ") and block.endswith("```"): return "code"
    # Quote
    if block.startswith("> "):
        check = check_quote(block)
        if check != -1: return check
    # Unordered list
    if block.startswith("* "):
        check = check_unordered_list("* ", block)
        if check != -1: return check
    if block.startswith("- "):
        check = check_unordered_list("- ", block)
        if check != -1: return check
    # ordered list
    if block.startswith("1. "):
        check = check_ordered_list(block)
        if check != -1: return check
    
    return "paragraph"

def markdown_to_html_node(markdown):
    # TODO
    # converts full md doc to single parent HTML Node
    # with many child HTMLNode objects
    # split the markdown into blocks
    # loop over each block
    # determine the type of block
    # based on the block type, create a new HTMLNode with the proper data
    # assign the proper child HTMLNode objects to the block node
    # make all the block nodes children under the single parent HTMLNode which should just be a div, and return it
    pass