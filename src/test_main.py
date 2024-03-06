import unittest

from main import *
from textnode import TextNode
from leafnode import LeafNode

class TestMain(unittest.TestCase):

    # TEST: text_node_to_html_node

    def test_text_node_to_html_node_given_type_text(self):
        textnode = TextNode("Text", text_type_text)
        expected = LeafNode(None, "Text")
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)
        
    def test_text_node_to_html_node_given_type_bold(self):
        textnode = TextNode("Bold Text", text_type_bold)
        expected = LeafNode("b", "Bold Text")
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)
    
    def test_text_node_to_html_node_given_type_italic(self):
        textnode = TextNode("Italic Text", text_type_italic)
        expected = LeafNode("i", "Italic Text")
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)
    
    def test_text_node_to_html_node_given_type_code(self):
        textnode = TextNode("Code", text_type_code)
        expected = LeafNode("code", "Code")
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)
    
    def test_text_node_to_html_node_given_type_link(self):
        textnode = TextNode("Link", text_type_link, "https://www.google.com")
        expected = LeafNode("a", "Link", {"href":"https://www.google.com"})
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)
    
    def test_text_node_to_html_node_given_type_image(self):
        textnode = TextNode("Image", text_type_image, "https://www.google.com")
        expected = LeafNode(None, "", {"src":"https://www.google.com", "alt":"Image"})
        actual = text_node_to_html_node(textnode)
        self.assertEqual(expected, actual)

    # TEST: split_nodes_delimiter

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
    
    def test_split_nodes_delimiter_given_mixed_delim_and_valid_split(self):
        textnode = TextNode("the red fox **jumped** *over* the `lazy` dog", text_type_text)
        expected = [
            TextNode("the red fox **jumped** ", text_type_text),
            TextNode("over", text_type_italic),
            TextNode(" the `lazy` dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "*", text_type_italic)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_mixed_delim_and_invalid_split(self):
        textnode = TextNode("the red fox **jumped** *over the `lazy` dog", text_type_text)
        self.assertRaises(Exception, split_nodes_delimiter([textnode], None, text_type_italic))