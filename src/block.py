

def markdown_to_blocks(markdown):
    blocks = []
    markdown_split = markdown.split("\n\n")
    for element in markdown_split:
        element = element.strip()
        if element:
            blocks.append(element)

    
    return blocks