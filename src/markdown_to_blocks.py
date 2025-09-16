from pydoc import text
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

def text_to_children_li(text: str) -> list[HTMLNode]:
    text_nodes = text_to_text_nodes(text)
    children = []

    for text_node in text_nodes:
        child_node = text_node_to_html_node(text_node)
        children.append(child_node)
    li_node = ParentNode("li", children)
    return [li_node]

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
            children = text_to_children(block.strip('# ').strip())
            html_node.add_child(ParentNode(f"h{block.count('#')}", children=children))
        elif block_type == BlockType.CODE:
            block_without_backticks = block.strip('`')
            removed_first_break = block_without_backticks[1:] if block_without_backticks.startswith('\n') else block_without_backticks
            text_node = TextNode(removed_first_break.replace("\n", "<br/>"), text_type=TextType.CODE_TEXT)
            child_node = text_node_to_html_node(text_node)
            html_node.add_child(ParentNode("pre", children=[child_node]))
        elif block_type == BlockType.QUOTE:
            children = []
            for line in block.split("\n"):
                if line.strip() == "":
                    continue
                children.append(LeafNode(None, line.strip("> ")+"<br/>"))
            html_node.add_child(ParentNode("blockquote", children=children))
        elif block_type == BlockType.UNORDERED_LIST:
            children_all = []
            for line in block.split("- "):
                if line.strip() == "":
                    continue
                children = text_to_children_li(line)
                children_all.extend(children)
            ul_node = ParentNode("ul", children=children_all)
            html_node.add_child(ul_node)
        elif block_type == BlockType.ORDERED_LIST:
            children_all = []
            for line in block.split("\n"):
                if line.strip() == "":
                    continue
                children = text_to_children_li(line.replace(re.match(r"^\d+\.\s+", line).group(0), ""))
                children_all.extend(children)
            ol_node = ParentNode("ol", children=children_all)
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