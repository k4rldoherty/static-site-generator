import unittest
from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]        
        )
        node2 = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                ParentNode("span", [LeafNode("bold", "Inner text")]),
            ]        
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

        self.assertEqual(
            node2.to_html(),
            "<div><b>Bold text</b>Normal text<i>italic text</i><span><bold>Inner text</bold></span></div>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    

    
if __name__ == "__main__":
    unittest.main()
