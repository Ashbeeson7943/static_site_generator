import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This should not be equal", TextType.BOLD)
        node2 = TextNode("This shoudl not be equal", TextType.PLAIN)
        self.assertNotEqual(node,node2)
    
    def test_no_url(self):
        node = TextNode("Url is a blank string", TextType.PLAIN)
        self.assertIsNone(node.url)
    
    def test_has_url(self):
        url = "https://testsite.com"
        node = TextNode("Url exists", TextType.ITALIC, url)
        self.assertEqual(node.url, url)

if __name__ == "__main__":
    unittest.main()