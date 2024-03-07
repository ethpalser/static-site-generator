import re
from parentnode import ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    if not isinstance(markdown, str):
        raise Exception("Cannot convert non-string text into blocks")
    return markdown.split("\n\n")

def block_to_block_type(block):
    if re.search(r"^[#]{1,6}\s{1}.*", block) is not None:
        return block_type_heading
    elif re.search(r"^```[\w\s]*```$", block) is not None:
        return block_type_code
    elif re.search(r"^\>\s.*", block) is not None:
        lines = block.split("\n")
        for line in lines:
            if re.search(r"^>\s.*", line) is None:
                return block_type_paragraph
        return block_type_quote
    elif re.search(r"^[*-]\s.*", block) is not None:
        lines = block.split("\n")
        for line in lines:
            if re.search(r"^[*-]\s.*", line) is None:
                return block_type_paragraph
        return block_type_unordered_list
    elif re.search(r"^[0-9]\.\s.*", block) is not None:
        lines = block.split("\n")
        num = 1
        for line in lines:
            if re.search(r"^[0-9]\.\s.*", line) is None or line[:len(f"{num}")] != f"{num}":
                return block_type_paragraph
            num += 1
        return block_type_ordered_list
    return block_type_paragraph