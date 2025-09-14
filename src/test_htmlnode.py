from htmlnode import HTMLNode 
import unittest 

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"class": "my-class"})
        self.assertEqual(repr(node), "tag='div', value='Hello, World!', children=[], props={'class': 'my-class'}")

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')
    
    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "http://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="http://example.com" target="_blank"')
