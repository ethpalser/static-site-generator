import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_given_no_prop(self):
        leaf = LeafNode("p", "Hello World")
        expected = "<p>Hello World</p>"
        actual = leaf.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_prop(self):
        leaf = LeafNode("a", "google.com", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">google.com</a>"
        actual = leaf.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_no_tag(self):
        leaf = LeafNode(None, "The sky is falling!")
        expected = "The sky is falling!"
        actual = leaf.to_html()
        self.assertEqual(expected, actual)