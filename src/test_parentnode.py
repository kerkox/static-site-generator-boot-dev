from parentnode import ParentNode
from leafnode import LeafNode
import unittest


class TestParentNode(unittest.TestCase):


    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node.to_html()
        assert node.to_html() == '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'

    def test_parent_node_empty(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_nested_nodes(self):
        child_node = ParentNode(
            "section",
            [
                LeafNode("span", "Span test"),
                ParentNode("div", [LeafNode("p", "This is a test.")]),
            ],
        )
        parent = ParentNode("div", [child_node])
        assert parent.to_html() == '<div><section><span>Span test</span><div><p>This is a test.</p></div></section></div>'