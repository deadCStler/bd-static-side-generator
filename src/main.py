from src.inline.inline_markdown import split_nodes_delimiter
from src.nodes.textnode import TextNode, TextType


def main():
    text_node = TextNode(
        "this is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    main()
