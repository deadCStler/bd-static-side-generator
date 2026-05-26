import unittest

from src.nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_fields(self):
        node = HTMLNode("strong", "Boot.dev")
        node2 = HTMLNode("strong", "Boot.dev")

        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_default_values(self):
        node = HTMLNode()
        node2 = HTMLNode()

        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, node2.props)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode("a", "Google", props=props)

        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_error_to_html(self):
        node = HTMLNode("strong", "Boot.dev")
        with self.assertRaises(NotImplementedError):
            node.to_html()
