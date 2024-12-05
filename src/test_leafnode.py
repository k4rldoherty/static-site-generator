import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        node = LeafNode(
            "div",
            "Hello, World!",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            "<div class=\"greeting\" href=\"https://boot.dev\">Hello, World!</div>"
        )

    def test_values(self):
        node = LeafNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            "div",
            node.tag,
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.props,
            None,
        )


if __name__ == "__main__":
    unittest.main()
