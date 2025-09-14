from leafnode import LeafNode
import unittest 

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), '<p>Hello, World!</p>')
    
    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, World!", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Hello, World!</span>')
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, World!", props={"id": "main"})
        self.assertEqual(node.to_html(), '<div id="main">Hello, World!</div>')

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Bold Text")
        self.assertEqual(node.to_html(), '<b>Bold Text</b>')
