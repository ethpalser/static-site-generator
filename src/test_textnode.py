import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        nodeA = TextNode("The world is your oyster", "bold", "")
        nodeB = TextNode("The world is your oyster", "bold", "")
        self.assertEqual(nodeA, nodeB)

if __name__ == "__main__":
    unittest.main()