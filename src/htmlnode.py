
class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props    

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        html = []
        for key in self.props:
            html.append(f"{key}=\"{self.props[key]}\"")
        return " ".join(html)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Missing Value")
        if self.tag is None:
            return self.value

        prop = ""
        if self.props is not None:
            prop = f" {self.props_to_html()}"

        return f"<{self.tag}{prop}>{self.value}</{self.tag}>"

        
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing Tag")
        if self.children is None:
            raise ValueError("Missing children")    

        html = [f"<{self.tag}>"]

        for child in self.children:
            html.append(child.to_html())

        html.append(f"</{self.tag}>")
        return "".join(html)
