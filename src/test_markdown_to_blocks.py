import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from block_type import BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_headers(self):
        text = """# Header 1

        This is a paragraph under header 1.

        ## Header 2

        This is a paragraph under header 2.
        """
        result = markdown_to_blocks(text)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "# Header 1")
        self.assertEqual(result[1], "This is a paragraph under header 1.")
        self.assertEqual(result[2], "## Header 2")
        self.assertEqual(result[3], "This is a paragraph under header 2.")

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Header 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```python\nprint('Hello, World!')\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- This is a list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is an ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_multiple_items(self):
        text = """
- Item 1
- Item 2
- Item 3
"""
        result = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(result[0]), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list_multiple_items(self):
        text = """
1. Item 1
2. Item 2
3. Item 3
"""
        result = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(result[0]), BlockType.ORDERED_LIST)
        