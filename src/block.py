

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
    if block[0:3] == "```" and block[-3:] == "```": return "code"
    # Quote
    if "> " in block:
        check = check_quote(block)
        if check != -1: return check
    # Unordered list
    if "* " in block:
        check = check_unordered_list("* ", block)
        if check != -1: return check
    if "- " in block:
        check = check_unordered_list("- ", block)
        if check != -1: return check
    # ordered list
    if block.startswith("1. "):
        check = check_ordered_list(block)
        if check != -1: return check
    
    return "paragraph"


def check_unordered_list(symbol, block):
    for b in block.split("\n"):
        if b and not b.startswith(symbol):
            return -1
    return "unordered_list"

def check_ordered_list(block):
    block_split = block.split("\n")
    for i in range(1, len(block_split)):
        if block_split[i] and not block_split[i].startswith(f"{i+1}. "):
            return -1
    return "ordered_list"

def check_header(block):
    valid_starts = ["###### ", "##### ", "#### ", "### ", "## ", "# "]
    for start in valid_starts:
        if block.startswith(start):
            if bool(block.split(" ", 1)[1].strip()):
                return "heading"
    return -1

def check_quote(block):
    for b in block.split("\n"):
        if b and b[0:2] != "> ":
            return -1
        
    return "quote"

def markdown_to_html_node(markdown):
    # converts full md doc to single parent HTML Node
    #
    pass