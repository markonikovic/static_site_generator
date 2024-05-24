import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.test_obj = HTMLNode()
        self.test_obj2 = HTMLNode(None, None, None,
                                  {"href": "https://www.google.com",
                                   "target": "_blank"})

    def test_raise_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.test_obj.to_html()

    def test_props_to_node_html(self):
        self.assertEqual(self.test_obj.props_to_html(), None)

    def test_props_to_node_html2(self):
        self.assertEqual(self.test_obj2.props_to_html(),
                         "href='https://www.google.com' target='_blank'")


if __name__ == "__main__":
    unittest.main()
