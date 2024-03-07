import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        nodeA = TextNode("The world is your oyster", "bold", "")
        nodeB = TextNode("The world is your oyster", "bold", "")
        self.assertEqual(nodeA, nodeB)

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

if __name__ == "__main__":
    unittest.main()