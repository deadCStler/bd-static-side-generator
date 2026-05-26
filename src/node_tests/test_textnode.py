import unittest

from src.nodes.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_diff_text(self):
        node = TextNode("This is a text node with a diff text", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_diff_textype(self):
        node = TextNode("This is text node", TextType.TEXT)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is text node", TextType.BOLD, "https:url")
        node2 = TextNode("This is text node", TextType.BOLD, "https:url")
        self.assertEqual(node, node2)

    def test_eq_diff_url(self):
        node = TextNode("This is text node", TextType.BOLD, "https:url")
        node2 = TextNode("This is text node", TextType.BOLD, "https:://url")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/image.png", "alt": "An image"},
        )


# if __name__ == "__main__":
#     unittest.main()
