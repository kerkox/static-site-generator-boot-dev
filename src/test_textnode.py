import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertTrue(node == node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertIsNone(node.url)
    
    def test_text_type_is_link(self):
        node = TextNode("This is a link", TextType.LINKS, url="http://example.com")
        self.assertEqual(node.text_type, TextType.LINKS)
        self.assertEqual(node.url, "http://example.com")

    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is another text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()