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

    def test_text_to_text_nodes_with_italic(self):
        text = "This is an _italic_ text"
        result = text_to_text_nodes(text)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[1].text_type, TextType.ITALIC_TEXT)


    def test_text_to_text_nodes_image_and_link(self):
        text = "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_text_nodes(text)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[1].text, "obi wan image")
        self.assertEqual(result[1].url, "https://i.imgur.com/fJRm4Vk.jpeg")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[2].text, " and a ")
        self.assertEqual(result[3].text, "link")
        self.assertEqual(result[3].url, "https://boot.dev")
        self.assertEqual(result[3].text_type, TextType.LINKS)


    def test_text_to_text_nodes_combine(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_text_nodes(text)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "text")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(result[2].text, " with an ")
        self.assertEqual(result[3].text, "italic")
        self.assertEqual(result[3].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(result[4].text, " word and a ")
        self.assertEqual(result[5].text, "code block")
        self.assertEqual(result[5].text_type, TextType.CODE_TEXT)
        self.assertEqual(result[6].text, " and an ")
        self.assertEqual(result[7].text, "obi wan image")
        self.assertEqual(result[7].text_type, TextType.IMAGE)
        self.assertEqual(result[8].text, " and a ")
        self.assertEqual(result[9].text, "link")
        self.assertEqual(result[9].url, "https://boot.dev")
        self.assertEqual(result[9].text_type, TextType.LINKS)