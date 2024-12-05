import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from utils import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node(self):
        node = TextNode("Image Node", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node,
            LeafNode("img", "", {'src': 'www.google.com', 'alt': 'Image Node'})
        )
        
        node2 = TextNode("Code Node", TextType.CODE)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(
            html_node2,
            LeafNode("code", "Code Node", None)
        )


if __name__ == "__main__":
    unittest.main()
