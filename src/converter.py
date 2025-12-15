
from textnode import TextNode, TextType
from splitters import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = []
    nodes.append(TextNode(text, TextType.TEXT))
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes