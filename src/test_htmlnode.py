import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
        
        def test_leaf_to_html_p(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        def test_leaf_to_html_a(self):
            node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("span", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "hi")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_single_child_no_arr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", child_node)
        self.assertRaises(TypeError, parent_node.to_html)

if __name__ == "__main__":
    unittest.main()