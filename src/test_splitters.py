import unittest

from splitters import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitters(unittest.TestCase):

    def test_split_nodes_delimiter_code(self):
        node      = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),
                                         TextNode(" word", TextType.TEXT) ])
    
    def test_split_nodes_multiple_internal(self):
        node      = TextNode("This is text with two `code` `block` words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [TextNode("This is text with two ", TextType.TEXT), TextNode("code", TextType.CODE),
                                         TextNode(" ", TextType.TEXT, None), TextNode("block", TextType.CODE),
                                         TextNode(" words", TextType.TEXT) ])
        
    def test_split_nodes_delimiter_italic(self):
        node      = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("italic block", TextType.ITALIC),
                                         TextNode(" word", TextType.TEXT) ])
        
    def test_split_nodes_delimiter_bold(self):
        node      = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("bold block", TextType.BOLD),
                                         TextNode(" word", TextType.TEXT) ])

    def test_split_nodes_delimiter_multple_types(self):
        node_italic  = TextNode("I am _italic_", TextType.TEXT)
        node_code    = TextNode("I am `code`", TextType.TEXT)
        node_bold    = TextNode("I am **bold**", TextType.TEXT)
        nodes        = [node_italic, node_bold, node_code]
        parsed_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        parsed_nodes = split_nodes_delimiter(parsed_nodes, "_", TextType.ITALIC)
        parsed_nodes = split_nodes_delimiter(parsed_nodes, "**", TextType.BOLD)
        self.assertListEqual(parsed_nodes, [TextNode("I am ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None),
                                            TextNode("", TextType.TEXT, None), TextNode("I am ", TextType.TEXT, None),
                                            TextNode("bold", TextType.BOLD, None), TextNode("", TextType.TEXT, None),
                                            TextNode("I am ", TextType.TEXT, None), TextNode("code", TextType.CODE, None),
                                            TextNode("", TextType.TEXT, None)])


if __name__ == "__main__":
    unittest.main()


