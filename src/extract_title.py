
def extract_title(markdown_content: str) -> str:
    """
    Extracts the title from the given markdown content.
    The title is assumed to be the first line that starts with '# '.

    Args:
        markdown_content (str): The markdown content as a string.

    Returns:
        str: The extracted title, or 'Untitled' if no title is found.
    """
    for line in markdown_content.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No title found in the markdown content.")