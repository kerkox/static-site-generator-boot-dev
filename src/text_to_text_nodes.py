from extract_markdown import split_nodes_image, split_nodes_link
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_text_nodes(text: str) -> list[TextNode]:
    text_node = TextNode(text=text, text_type=TextType.TEXT)
    result = split_nodes_delimiter([text_node], "**", TextType.BOLD_TEXT)
    result = split_nodes_delimiter(result, "`", TextType.CODE_TEXT)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC_TEXT)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

