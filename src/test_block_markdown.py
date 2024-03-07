import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    block_to_heading_html_node,
    block_to_code_html_node,
    block_to_quote_html_node,
    block_to_unordered_list_html_node,
    block_to_ordered_list_html_node,
    block_to_paragraph_html_node,
    markdown_to_html_node
)
from parentnode import ParentNode
from leafnode import LeafNode

class TestBlockMarkdown(unittest.TestCase):

    # TEST markdown_to_blocks

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

    # TEST block_to_block_type

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

    # TEST block_to_*_html_node

    def block_to_heading_html_node(self):
        block = "### Heading 3"
        expected = ParentNode("h3", None, [LeafNode(None, "Heading 3")])
        actual = block_to_heading_html_node(block)
        self.assertEqual(expected, actual)
        
    def test_block_to_code_html_node(self):
        block = "```Code Line 1\nCode Line 2```"
        expected = ParentNode("pre", None, [LeafNode("code", "Code Line 1\nCode Line 2")])
        actual = block_to_code_html_node(block)
        self.assertEqual(expected, actual)

    def test_block_to_quote_html_node(self):
        block = "> Quote Line 1\n> Quote Line 2\n> Quote Line 3"
        expected = ParentNode("blockquote", None, [LeafNode(None, "Quote Line 1\nQuote Line 2\nQuote Line 3")])
        actual = block_to_quote_html_node(block)
        self.assertEqual(expected, actual)

    def test_block_to_unordered_list_html_node(self):
        block = "* Asterisk 1\n* Asterisk 2\n- Dash"
        expected = ParentNode("ul", None, [
            ParentNode("li", None, [LeafNode(None, "Asterisk 1")]),
            ParentNode("li", None, [LeafNode(None, "Asterisk 2")]),
            ParentNode("li", None, [LeafNode(None, "Dash")])
        ])
        actual = block_to_unordered_list_html_node(block)
        self.assertEqual(expected, actual)

    def test_block_to_ordered_list_html_node(self):
        block = "1. One\n2. Two\n3. Three"
        expected = ParentNode("ol", None, [
            ParentNode("li", None, [LeafNode(None, "One")]),
            ParentNode("li", None, [LeafNode(None, "Two")]),
            ParentNode("li", None, [LeafNode(None, "Three")])
        ])
        actual = block_to_ordered_list_html_node(block)
        self.assertEqual(expected, actual)

    def test_block_to_paragraph_html_node(self):
        block = "The red **fox** *jumped* over the `lazy` dog"
        expected = ParentNode("p", None, [
            LeafNode(None, "The red "),
            LeafNode("b", "fox"),
            LeafNode(None, " "),
            LeafNode("i", "jumped"),
            LeafNode(None, " over the "),
            LeafNode("code", "lazy"),
            LeafNode(None, " dog")
        ])
        actual = block_to_paragraph_html_node(block)
        self.assertEqual(expected, actual)

    # TEST markdown_to_html_node

    def test_markdown_to_html_node(self):
        markdown = """### Heading 3

```Code Line 1\nCode Line 2```

> Quote Line 1\n> Quote Line 2\n> Quote Line 3

* Asterisk 1\n* Asterisk 2\n- Dash

1. One\n2. Two\n3. Three

The red **fox** *jumped* over the `lazy` dog"""
        expected = ParentNode("div", None, [
            ParentNode("h3", None, [LeafNode(None, "Heading 3")]),
            ParentNode("pre", None, [LeafNode("code", "Code Line 1\nCode Line 2")]),
            ParentNode("blockquote", None, [LeafNode(None, "Quote Line 1\nQuote Line 2\nQuote Line 3")]),
            ParentNode("ul", None, [
                ParentNode("li", None, [LeafNode(None, "Asterisk 1")]),
                ParentNode("li", None, [LeafNode(None, "Asterisk 2")]),
                ParentNode("li", None, [LeafNode(None, "Dash")])
            ]),
            ParentNode("ol", None, [
                ParentNode("li", None, [LeafNode(None, "One")]),
                ParentNode("li", None, [LeafNode(None, "Two")]),
                ParentNode("li", None, [LeafNode(None, "Three")])
            ]),
            ParentNode("p", None, [
                LeafNode(None, "The red "),
                LeafNode("b", "fox"),
                LeafNode(None, " "),
                LeafNode("i", "jumped"),
                LeafNode(None, " over the "),
                LeafNode("code", "lazy"),
                LeafNode(None, " dog")
            ])
        ])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)