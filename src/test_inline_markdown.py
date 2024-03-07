import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

class TestInlineMarkdown(unittest.TestCase):

    def test_split_nodes_delimiter_given_no_delim(self):
        textnode = TextNode("the red fox jumped over the lazy dog", text_type_text)
        expected = [textnode]
        actual = split_nodes_delimiter([textnode], None, text_type_text)
        self.assertEqual(expected, actual)

    def test_split_nodes_delimiter_given_bold_delim(self):
        textnode = TextNode("the red fox **jumped** over the lazy dog", text_type_text)
        expected = [
            TextNode("the red fox ", text_type_text),
            TextNode("jumped", text_type_bold),
            TextNode(" over the lazy dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "**", text_type_bold)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_italic_delim(self):
        textnode = TextNode("the red fox jumped *over* the lazy dog", text_type_text)
        expected = [
            TextNode("the red fox jumped ", text_type_text),
            TextNode("over", text_type_italic),
            TextNode(" the lazy dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "*", text_type_italic)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_code_delim(self):
        textnode = TextNode("the red fox jumped over the `lazy` dog", text_type_text)
        expected = [
            TextNode("the red fox jumped over the ", text_type_text),
            TextNode("lazy", text_type_code),
            TextNode(" dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "`", text_type_code)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_mixed_delim_and_invalid_split(self):
        textnode = TextNode("the red fox **jumped** *over the `lazy` dog", text_type_text)
        self.assertRaises(Exception, split_nodes_delimiter([textnode], None, text_type_italic))

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)