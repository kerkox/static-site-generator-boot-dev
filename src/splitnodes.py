from textnode import TextNode, TextType

"""
Splits text nodes by a delimiter and returns a new list of text nodes.
example:
node = TextNode("This is text with a `code block` word aditional `this another code`", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

new_nodes becomes:
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word aditional ", TextType.TEXT),
    TextNode("this another code", TextType.CODE),
]
"""
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if(node.text.count(delimiter) % 2 != 0):
            raise Exception(f"Unmatched delimiter {delimiter} in text: {node.text}")
        tmp_text = node.text
        while tmp_text.count(delimiter) >= 2:
            start_index = tmp_text.index(delimiter)
            delimiter_length = len(delimiter)
            end_index = tmp_text.index(delimiter, start_index + delimiter_length)
            before = tmp_text[:start_index]
            code = tmp_text[start_index + delimiter_length:end_index]
            after = tmp_text[end_index + delimiter_length:]
            if before:
                new_nodes.append(TextNode(before, node.text_type))
            new_nodes.append(TextNode(code, text_type))
            tmp_text = after
        if tmp_text:
            new_nodes.append(TextNode(tmp_text, node.text_type))
    return new_nodes