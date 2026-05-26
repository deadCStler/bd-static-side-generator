import unittest

from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode


class Test_ParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child_node_span = LeafNode("span", "child1")
        child_node_div = LeafNode("div", "child2")
        parent_node = ParentNode("div", [child_node_span, child_node_div])
        self.assertEqual(
            parent_node.to_html(), "<div><span>child1</span><div>child2</div></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_with_props(self):
        child_node_a = LeafNode("a", "Google.com", {"href": "https://www.google.com"})
        child_node_div = LeafNode("div", "div_child")
        parent_node = ParentNode("div", [child_node_a, child_node_div])
        self.assertEqual(
            parent_node.to_html(),
            '<div><a href="https://www.google.com">Google.com</a><div>div_child</div></div>',
        )

    def test_error_no_child_to_html(self):
        node = ParentNode("strong", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_error_no_tag_to_html(self):
        child_node_div = LeafNode("div", "div_child")
        node = ParentNode(None, [child_node_div])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_mixed_tagged_and_raw_text_children(self):
        raw_text = LeafNode(None, "plain text")
        tagged_child = LeafNode("span", "inside span")
        parent = ParentNode("p", [raw_text, tagged_child])
        self.assertEqual(parent.to_html(), "<p>plain text<span>inside span</span></p>")

    def test_to_html_with_multiple_raw_and_tagged_children(self):
        raw1 = LeafNode(None, "start")
        span = LeafNode("span", "middle")
        raw2 = LeafNode(None, " end")
        parent = ParentNode("div", [raw1, span, raw2])
        self.assertEqual(parent.to_html(), "<div>start<span>middle</span> end</div>")

    def test_to_html_with_parent_tag_p(self):
        child = LeafNode("em", "italic")
        parent = ParentNode("p", [child])
        self.assertEqual(parent.to_html(), "<p><em>italic</em></p>")

    def test_to_html_with_parent_tag_div(self):
        child = LeafNode("span", "content")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>content</span></div>")

    def test_to_html_with_parent_tag_h2(self):
        child = LeafNode("strong", "bold heading")
        parent = ParentNode("h2", [child])
        self.assertEqual(parent.to_html(), "<h2><strong>bold heading</strong></h2>")

    def test_to_html_with_parent_tag_ul(self):
        li_child = LeafNode("li", "list item")
        parent = ParentNode("ul", [li_child])
        self.assertEqual(parent.to_html(), "<ul><li>list item</li></ul>")

    def test_to_html_with_leaf_and_parent_children_same_level(self):
        leaf_node = LeafNode("span", "leaf child")
        parent_child = ParentNode("strong", [LeafNode("i", "nested italic")])
        another_leaf = LeafNode("a", "link", {"href": "https://example.com"})
        parent = ParentNode("div", [leaf_node, parent_child, another_leaf])
        self.assertEqual(
            parent.to_html(),
            '<div><span>leaf child</span><strong><i>nested italic</i></strong><a href="https://example.com">link</a></div>',
        )

    def test_to_html_with_parent_child_containing_leaf_and_sibling_leaf(self):
        inner_parent = ParentNode("em", [LeafNode(None, "raw inside")])
        sibling_leaf = LeafNode("b", "bold sibling")
        parent = ParentNode("section", [inner_parent, sibling_leaf])
        self.assertEqual(
            parent.to_html(),
            "<section><em>raw inside</em><b>bold sibling</b></section>",
        )
