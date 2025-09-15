import re

from block_type import BlockType
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_text_nodes import text_to_text_nodes
from converters import text_node_to_html_node


def markdown_to_blocks(text: str) -> list[str]:
    text_blocks = []
    blocks = text.split("\n\n")
    for block in blocks:
        if len(block.strip()) != 0:
            text_blocks.append(block.strip())
    return text_blocks

def block_to_block_type(block: str) -> BlockType:
    heading_re = re.search(r"^(#{1,6})\s+(.*)", block, re.DOTALL)
    if heading_re is not None:
        return BlockType.HEADING
    code_re = re.search(r"^`(.*)`$", block, re.DOTALL)
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

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        child_node = text_node_to_html_node(text_node)
        children.append(child_node)
    return children

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_node = ParentNode("div")
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            html_node.add_child(LeafNode(f"h{block.count('#')}", block.strip('# ').strip()))
        elif block_type == BlockType.CODE:
            block_without_backticks = block.strip('`')
            removed_first_break = block_without_backticks[1:] if block_without_backticks.startswith('\n') else block_without_backticks
            text_node = TextNode(removed_first_break, text_type=TextType.CODE_TEXT)
            child_node = text_node_to_html_node(text_node)
            html_node.add_child(ParentNode("pre", children=[child_node]))
        elif block_type == BlockType.QUOTE:
            html_node.add_child(LeafNode("blockquote", block.strip('> ')))
        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = ParentNode("ul")
            for item in block.split("\n"):
                ul_node.add_child(LeafNode("li", item.strip('- ')))
            html_node.add_child(ul_node)
        elif block_type == BlockType.ORDERED_LIST:
            ol_node = ParentNode("ol")
            for item in block.split("\n"):
                text = re.search(r"^\d+\.\s+(.*)", item)
                ol_node.add_child(LeafNode("li", text.group(1) if text else item))
            html_node.add_child(ol_node)
        else:
            text_nodes = text_to_text_nodes(block)
            parent_node = ParentNode("p")
            for text_node in text_nodes: 
                text_node.text = text_node.text.replace('\n', ' ')
                child_node = text_node_to_html_node(text_node)
                parent_node.add_child(child_node)
            html_node.add_child(parent_node)
    return html_node