import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        htmlnodeA = HTMLNode("p", "text")
        self.assertIsNone(htmlnodeA.props_to_html())

        htmlnodeB = HTMLNode("a", "google.com", None, {"href": "https://www.google.com"})
        self.assertIsNotNone(htmlnodeB.props_to_html())


class TestParentNode(unittest.TestCase):

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