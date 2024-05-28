import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.test_obj = LeafNode("p", "Hello Marko.")
        self.test_obj2 = LeafNode("p", None)
        self.test_obj3 = LeafNode(None, "There is no tag")

    def testToHTML(self):
        self.assertEqual(self.test_obj.to_html(), "<p>Hello Marko.</p>")

    def testToHTML2(self):
        with self.assertRaises(ValueError):
            self.test_obj2.to_html()

    def testNoTag(self):
        self.assertEqual(self.test_obj3.to_html(), "There is no tag")
