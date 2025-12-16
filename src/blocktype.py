from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md_block):
    md_block_lines = md_block.split("\n")
    amount_of_lines = len(md_block_lines)

    return_type = ""
    # Heading check
    return_type = is_heading_block(md_block)
    if type_found(return_type):
        return return_type
    # code check
    return_type = is_code_block(md_block)
    if type_found(return_type):
        return return_type
    # quote check
    return_type = is_quote_block(md_block_lines, amount_of_lines)
    if type_found(return_type):
        return return_type
    # unordered check
    return_type = is_unordered_block(md_block_lines, amount_of_lines)
    if type_found(return_type):
        return return_type
    # ordered check
    return_type = is_ordered_block(md_block_lines, amount_of_lines)
    if type_found(return_type):
        return return_type
    
    if return_type is None:
        return_type = BlockType.PARAGRAPH
    return return_type

def type_found(block_type):
    return block_type is not None

def is_heading_block(md_block):
    if "# " in md_block[:7]:
        return BlockType.HEADING
    
def is_code_block(md_block):
    if md_block[:3] == "```" and md_block[-3:] == "```":
        return BlockType.CODE

def is_quote_block(md_block_lines, amount_of_lines):
    qc = 0
    for line in md_block_lines:
        if ">" in line[:1]:
          qc += 1
    if qc == amount_of_lines:
        return BlockType.QUOTE
    
def is_unordered_block(md_block_lines, amount_of_lines):
    qc = 0
    for line in md_block_lines:
        if "- " in line[:2]:
          qc += 1
    if qc == amount_of_lines:
        return BlockType.UNORDERED_LIST

def is_ordered_block(md_block_lines, amount_of_lines):
    qc = 0
    for line in md_block_lines:
        if re.search(r"(\d+\. )", line):
          qc += 1
    if qc == amount_of_lines:
        return BlockType.ORDERED_LIST