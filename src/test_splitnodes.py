import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word aditional `this another code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE_TEXT)
        self.assertEqual(new_nodes[2].text, " word aditional ")
        self.assertEqual(new_nodes[3].text, "this another code")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE_TEXT)