import unittest
from src.block import markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type(self):
        code = "``` This is a code ```"
        quote = """> This is a quote
> It can span multiple lines
> Each line must start with >"""
        unordered_list = """* First item
* Second item
* Third item
"""
        ordered_list = """1. First item
2. Second item
3. Third item
"""
        header = "## Header"

        self.assertEqual(block_to_block_type(code), "code")
        self.assertEqual(block_to_block_type(quote), "quote")
        self.assertEqual(block_to_block_type(unordered_list), "unordered_list")
        self.assertEqual(block_to_block_type(ordered_list), "ordered_list")
        self.assertEqual(block_to_block_type(header), "heading")

    def test_block_to_block_type_wrong(self):
        code = "`` This is a code ```"
        quote = """> This is a quote
It can span multiple lines
> Each line must start with >
"""
        unordered_list = """* First item
** Second item
* Third item
"""
        ordered_list = """1. First item
5. Second item
3. Third item
"""
        header = "### "

        self.assertNotEqual(block_to_block_type(code), "code")
        self.assertNotEqual(block_to_block_type(quote), "quote")
        self.assertNotEqual(block_to_block_type(unordered_list), "unordered_list")
        self.assertNotEqual(block_to_block_type(ordered_list), "ordered_list")
        self.assertNotEqual(block_to_block_type(header), "heading")
    
    def test_markdown_to_html(self):
        # Headers
        assert markdown_to_html_node("# Header 1") == '<div><h1>Header 1</h1></div>'
        assert markdown_to_html_node("## Header 2") == '<div><h2>Header 2</h2></div>'
        assert markdown_to_html_node("### Header *with italic*") == '<div><h3>Header <i>with italic</i></h3></div>'

        # Paragraphs
        assert markdown_to_html_node("Just a paragraph") == '<div><p>Just a paragraph</p></div>'
        assert markdown_to_html_node("""First paragraph
with multiple lines""") == '<div><p>First paragraph with multiple lines</p></div>'

        # Multiple paragraphs
        assert markdown_to_html_node("""First paragraph

Second paragraph""") == '<div><p>First paragraph</p><p>Second paragraph</p></div>'

        # Code blocks
        assert markdown_to_html_node("""```
code block
multiple lines
```""") == '<div><pre><code>code block\nmultiple lines</code></pre></div>'

        # Quotes
        assert markdown_to_html_node("""> quote line 1
> quote line 2""") == '<div><blockquote><p>quote line 1 quote line 2</p></blockquote></div>'
    
        assert markdown_to_html_node("""> para 1
> still para 1
>
> para 2""") == '<div><blockquote><p>para 1 still para 1</p><p>para 2</p></blockquote></div>'

        # Unordered lists
        assert markdown_to_html_node("""* item 1
* item 2
* item 3""") == '<div><ul><li>item 1</li><li>item 2</li><li>item 3</li></ul></div>'