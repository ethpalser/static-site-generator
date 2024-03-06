import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        htmlnodeA = HTMLNode("p", "text")
        self.assertIsNone(htmlnodeA.props_to_html())

        htmlnodeB = HTMLNode("a", "google.com", None, {"href": "https://www.google.com"})
        self.assertIsNotNone(htmlnodeB.props_to_html())
