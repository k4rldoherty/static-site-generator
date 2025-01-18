import unittest
from src.page_generation import extract_title

class TestPageGeneration(unittest.TestCase):
    def test_extract_title(self):
        test_md = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien
"""
        self.assertEqual(extract_title(test_md), "Tolkien Fan Club")