import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("tag", "value", None, {"href": "https://www.google.com", "target":"_blank"})
        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"')

    def test_defaults_to_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_string_representation(self):
        node = HTMLNode("Tag", "Value", "Children", {"Props":"props"})
        self.assertEqual(f"{node}", f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})")

if __name__ == "__main__":
    unittest.main()