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