import unittest
from src.block import markdown_to_blocks, block_to_block_type

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
> Each line must start with >
"""
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
