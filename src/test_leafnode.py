import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        leafnodeA = LeafNode("p", "Hello World")
        expectedA = "<p>Hello World</p>"
        actualA = leafnodeA.to_html()
        self.assertEqual(expectedA, actualA)

        leafnodeB = LeafNode("a", "google.com", {"href": "https://www.google.com"})
        expectedB = "<a href=\"https://www.google.com\">google.com</a>"
        actualB = leafnodeB.to_html()
        self.assertEqual(expectedB, actualB)

        leafnodeC = LeafNode(None, "The sky is falling!")
        expectedC = "The sky is falling!"
        actualC = leafnodeC.to_html()
        self.assertEqual(expectedC, actualC)