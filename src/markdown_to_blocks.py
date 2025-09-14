import re
from block_type import BlockType


def markdown_to_blocks(text: str) -> list[str]:
    text_blocks = []
    blocks = text.split("\n\n")
    for block in blocks:
        text_blocks.append(block.strip())
    return text_blocks

def block_to_block_type(block: str) -> BlockType:
    heading_re = re.search(r"^(#{1,6})\s+(.*)", block, re.DOTALL)
    if heading_re is not None:
        return BlockType.HEADING
    code_re = re.search(r"^```(.*)```$", block, re.DOTALL)
    if code_re is not None:
        return BlockType.CODE
    if block.startswith("> "):
        return BlockType.QUOTE
    unorder_list_re = re.search(r"^- (.*)", block, re.DOTALL)
    if unorder_list_re is not None:
        return BlockType.UNORDERED_LIST
    order_list_re = re.search(r"^\d+\.\s+(.*)", block, re.DOTALL)
    if order_list_re is not None:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
