import unittest

from converter import text_to_textnodes, markdown_to_blocks
from textnode import TextNode, TextType


class TestSplitters(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, [TextNode("This is ", TextType.TEXT),TextNode("text", TextType.BOLD),TextNode(" with an ", TextType.TEXT),TextNode("italic", TextType.ITALIC),
                                     TextNode(" word and a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" and an ", TextType.TEXT),TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                     TextNode(" and a ", TextType.TEXT),TextNode("link", TextType.LINK, "https://boot.dev")])
        
    def test_markdown_to_block(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is **bolded** paragraph", "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                                  "- This is a list\n- with items"])

if __name__ == "__main__":
    unittest.main()
