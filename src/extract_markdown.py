import re

from textnode import TextNode, TextType

def extract_markdown_images(text: str) -> list[str]:
    """Extrae URLs de imágenes en formato Markdown del texto dado."""

    pattern = r'!\[(.*?)\]\((.*?)\)'
    result = re.findall(pattern, text)
    return result

def extract_markdown_links(text: str) -> list[str]:
    """Extrae URLs de enlaces en formato Markdown del texto dado."""

    pattern = r'\[(.*?)\]\((.*?)\)'
    result = re.findall(pattern, text)
    return result


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    image_split_pattern = r'!\[.*?\]\(.*?\)'
    image_pattern = r'!\[(.*?)\]\((.*?)\)'

    for node in old_nodes:
        text = node.text
        if text is None or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(f'({image_split_pattern})', text)
        for part in parts:
            if re.match(image_pattern, part):
                alt_text, url = re.findall(r'!\[(.*?)\]\((.*?)\)', part)[0]
                new_nodes.append(TextNode(text=alt_text, text_type=TextType.IMAGE, url=url))
            elif part:
                new_nodes.append(TextNode(text=part, text_type=TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    link_split_pattern = r'\[.*?\]\(.*?\)'
    link_pattern = r'\[(.*?)\]\((.*?)\)'

    for node in old_nodes:
        text = node.text
        if text is None or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(f'({link_split_pattern})', text)
        for part in parts:
            if re.match(link_pattern, part):
                link_text, url = re.findall(r'\[(.*?)\]\((.*?)\)', part)[0]
                new_nodes.append(TextNode(text=link_text, text_type=TextType.LINKS, url=url))
            elif part:
                new_nodes.append(TextNode(text=part, text_type=TextType.TEXT))

    return new_nodes