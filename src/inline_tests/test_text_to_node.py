import unittest

from src.inline.text_to_nodes import text_to_textnodes
from src.nodes.textnode import TextNode, TextType


class Test_Text_to_Node(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_plain(self):
        text = "Just plain text"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("Just plain text", TextType.TEXT)],
            new_nodes,
        )

    def test_text_to_textnodes_only_bold(self):
        text = "**bold only**"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("bold only", TextType.BOLD)],
            new_nodes,
        )

    def test_text_to_textnodes_only_italic(self):
        text = "_italic only_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("italic only", TextType.ITALIC)],
            new_nodes,
        )

    def test_text_to_textnodes_only_code(self):
        text = "`code only`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("code only", TextType.CODE)],
            new_nodes,
        )

    def test_text_to_textnodes_only_image(self):
        text = "![alt](https://example.com/img.png)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("alt", TextType.IMAGE, "https://example.com/img.png")],
            new_nodes,
        )

    def test_text_to_textnodes_only_link(self):
        text = "[click](https://example.com)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("click", TextType.LINK, "https://example.com")],
            new_nodes,
        )

    def test_text_to_textnodes_bold_and_italic(self):
        text = "**bold** and _italic_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
