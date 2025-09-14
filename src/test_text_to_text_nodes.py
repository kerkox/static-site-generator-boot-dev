import unittest
from textnode import TextType
from text_to_text_nodes import text_to_text_nodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_text_nodes(self):
        text = "This is a **bold** text"
        result = text_to_text_nodes(text)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)
