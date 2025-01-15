def extract_title(markdown):
    md_split = markdown.split("\n")
    for line in md_split:
        if line.startswith("# "):
            return line.removeprefix("# ")
    raise ValueError("No heading has been found")