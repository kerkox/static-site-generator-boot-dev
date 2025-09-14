from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_text_nodes(text: str) -> list[TextNode]:
    text_node = TextNode(text=text, text_type=TextType.TEXT)
    result = split_nodes_delimiter([text_node], "**", TextType.BOLD_TEXT)
    return result


result = text_to_text_nodes("This is a **bold** text")
print(result)  # [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD_TEXT), TextNode(" text", TextType.TEXT)]