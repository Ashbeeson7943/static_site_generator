

from textnode import TextType, TextNode

# Only handles ONE delimter at once
# Does not handle delimiters inside of delimeters i.e. _Italic and **bold**_
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = []
        try:
            split_text = node.text.split(delimiter)
        except Exception:
            raise Exception(f"{delimiter} not found.")

        for i in range(0, len(split_text)):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes


