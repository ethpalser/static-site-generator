

def markdown_to_blocks(markdown):
    if not isinstance(markdown, str):
        raise Exception("Cannot convert non-string text into blocks")
    return markdown.split("\n\n")