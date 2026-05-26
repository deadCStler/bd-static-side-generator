from src.nodes.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag found")
        if not self.children:
            raise ValueError("No children tags found")
        inner_html = ""
        for node in self.children:
            inner_html += node.to_html()
        return f"<{self.tag}>{inner_html}</{self.tag}>"
