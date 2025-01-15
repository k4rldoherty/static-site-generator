from src.block_utils import check_header, check_ordered_list, check_quote, check_unordered_list
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.inline import text_node_to_html_node, text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for element in markdown_split:
        element = element.strip()
        if element:
            blocks.append(element)
    return blocks

def block_to_block_type(block):
    if block[0] == "#":
        check = check_header(block)
        if check != -1: return check
    # Code
    if block.startswith("```") and block.endswith("```"): return "code"
    # Quote
    if block.startswith(">"):
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
    blocks = markdown_to_blocks(markdown)
    html_node = ParentNode("div", children=[])
    # loop over each block
    for block in blocks:
        # determine the type of block
        block_type = block_to_block_type(block)
        # based on the block type, create a new HTMLNode with the proper data
        if block_type == "heading":
            node = create_header_node(block)
            html_node.children.append(node)
        
        elif block_type == "code":
            node = create_code_node(block)
            html_node.children.append(node)
        
        elif block_type == "quote":
            # create_quote_node(block)
            node = create_quote_node(block)
            html_node.children.append(node)

        elif block_type == "ordered_list":
            node = create_list_node(block, "ol")
            html_node.children.append(node)
        
        elif block_type == "unordered_list":
            node = create_list_node(block, "ul")
            html_node.children.append(node)
        
        elif block_type == "paragraph":
            lines = block.split("\n")
            processed_text = " ".join(lines)
            html_node.children.append(ParentNode("p", text_to_children(processed_text)))

    return html_node.to_html()

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for tn in text_nodes:
        html_nodes.append(text_node_to_html_node(tn))
    return html_nodes

def create_header_node(block):
    header_split = block.split(" ", 1)
    header_type = len(header_split[0])
    header_text = text_to_children(header_split[1].strip())
    return ParentNode(f"h{header_type}", header_text)

def create_code_node(block):
    code_content = block.strip().removeprefix("```").removesuffix("```").strip()
    code_node = ParentNode("code", text_to_children(code_content))
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def create_quote_node(block):
    quotes_split = block.split("\n")
    refined_lines = [q.split(">", 1)[1].strip() for q in quotes_split]
    node = ParentNode("blockquote", [])

    if "" in refined_lines or " " in refined_lines:
        # there is a paragraph break so every "" is a seperate <p> tag inside the <blockquote>
        result = []
        current_group = []
        for item in refined_lines:
            if item == "" or item == " ":
                if current_group:  # only append non-empty groups
                    result.append(current_group)
                    current_group = []
            else:
                current_group.append(item.strip())
        if current_group:  # don't forget the last group
            result.append(current_group)
        for r in result:
            node.children.append(ParentNode("p", text_to_children(" ".join(r).strip())))

    else:
        # there is no breaks so it is all one textnode inside the <blockquote>
        refined_line = " ".join(refined_lines).strip()
        node.children.append(ParentNode("p", text_to_children(refined_line)))

    return node

def create_list_node(block, type):
    list_split = block.split("\n")
    refined_list = []
    for i in list_split:
        refined_list.append(i.split(" ", 1)[1].strip())
    node = ParentNode(type, [])
    for item in refined_list:
        node.children.append(ParentNode("li", text_to_children(item.strip())))

    return node