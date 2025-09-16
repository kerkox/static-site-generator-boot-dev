from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not isinstance(text_node.text_type, TextType):
        raise Exception(f"Invalid TextType: {text_node.text_type}")
    text_node.text = text_node.text.replace("\n", "")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, props={"href": text_node.url if text_node.url else "#"})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url if text_node.url else "#", "alt": text_node.text})
        case _:
            raise ValueError(f"Unknown TextType: {text_node.text_type}")
