import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
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

    def test_block_to_block_type_given_heading(self):
        block = "### Heading 3"
        expected = block_type_heading
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_given_code_block(self):
        block = "```Code Line 1\nCode Line 2```"
        expected = block_type_code
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_block_type_given_quote(self):
        block = "> Quote Line 1\n> Quote Line 2\n> Quote Line 3"
        expected = block_type_quote
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_block_type_given_unordered_list(self):
        block = "* Asterisk 1\n* Asterisk 2\n- Dash"
        expected = block_type_unordered_list
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_block_type_given_ordered_list(self):
        block = "1. One\n2. Two\n3. Three"
        expected = block_type_ordered_list
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_block_type_given_disordered_list(self):
        block = "1. One\n3. Three\n2. Two"
        expected = block_type_paragraph
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_block_type_given_paragraph(self):
        block = "The red fox jumped over the red dog"
        expected = block_type_paragraph
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)