import unittest
from block_markdown import (
    markdown_to_blocks
)

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks_given_markdown(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_markdown_to_blocks_given_numbers(self):
        markdown = 123456789
        self.assertRaises(Exception, markdown_to_blocks, markdown)

    def test_markdown_to_blocks_given_numbers_as_string(self):
        markdown = "1234567890"
        expected = ["1234567890"]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)