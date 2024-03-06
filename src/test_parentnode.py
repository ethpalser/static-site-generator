import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_given_no_children(self):
        root = ParentNode("div", "Hello", None, None)
        expected = "<div>Hello</div>"
        actual= root.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_leaf_children(self):
        root = ParentNode("div", "Hello", [
            LeafNode("p", "Paragraph Text"),
            LeafNode(None, "Regular Text"),
            LeafNode("b", "Bold Text")
        ], None)

        expected = "<div>Hello<p>Paragraph Text</p>Regular Text<b>Bold Text</b></div>"
        actual = root.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_parent_children_with_no_children(self):
        root = ParentNode("div", "Hello", [
            ParentNode("div", "World"),
        ], None)

        expected = "<div>Hello<div>World</div></div>"
        actual = root.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_parent_children_with_leaf_children(self):
        root = ParentNode("div", "Hello", [
            ParentNode("div", "World", [
                LeafNode("p", "The sky is falling!")
            ]),
            LeafNode("a", "google.com", {"href": "https://www.google.com"})
        ], None)

        expected = "<div>Hello<div>World<p>The sky is falling!</p></div><a href=\"https://www.google.com\">google.com</a></div>"
        actual = root.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_given_no_tag(self):
        root = ParentNode(None, "Hello World")
        self.assertRaises(ValueError, root.to_html)