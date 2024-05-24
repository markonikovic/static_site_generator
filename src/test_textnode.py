import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "this is awsome")
        node2 = TextNode("This is a text node", "bold", "this is awsome")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Test", "italic", None)
        node2 = TextNode("Test", "italic", None)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("Test", "bold", None)
        node2 = TextNode("Test2", "bold", None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
