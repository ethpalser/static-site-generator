import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestInlineMarkdown(unittest.TestCase):

    # TEST split_nodes_delimiter

    def test_split_nodes_delimiter_given_no_delim(self):
        textnode = TextNode("the red fox jumped over the lazy dog", text_type_text)
        expected = [textnode]
        actual = split_nodes_delimiter([textnode], None, text_type_text)
        self.assertEqual(expected, actual)

    def test_split_nodes_delimiter_given_bold_delim(self):
        textnode = TextNode("the red fox **jumped** over the lazy dog", text_type_text)
        expected = [
            TextNode("the red fox ", text_type_text),
            TextNode("jumped", text_type_bold),
            TextNode(" over the lazy dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "**", text_type_bold)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_italic_delim(self):
        textnode = TextNode("the red fox jumped *over* the lazy dog", text_type_text)
        expected = [
            TextNode("the red fox jumped ", text_type_text),
            TextNode("over", text_type_italic),
            TextNode(" the lazy dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "*", text_type_italic)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_code_delim(self):
        textnode = TextNode("the red fox jumped over the `lazy` dog", text_type_text)
        expected = [
            TextNode("the red fox jumped over the ", text_type_text),
            TextNode("lazy", text_type_code),
            TextNode(" dog", text_type_text)
        ]
        actual = split_nodes_delimiter([textnode], "`", text_type_code)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_delimiter_given_mixed_delim_and_invalid_split(self):
        textnode = TextNode("the red fox **jumped** *over the `lazy` dog", text_type_text)
        self.assertRaises(Exception, split_nodes_delimiter([textnode], None, text_type_italic))

    # TEST extract_markdown_images

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

    # TEST extract_markdown_links

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)    

    # TEST split_nodes_image

    def test_split_nodes_image_given_image(self):
        node = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![another](https://i.imgur.com/dfsdkjfd.png)", text_type_text)]
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("another", text_type_image, "https://i.imgur.com/dfsdkjfd.png")
        ]
        actual = split_nodes_image(node)
        self.assertEqual(expected, actual)

    # TEST split_nodes_link

    def test_split_nodes_link_given_link(self):
        node = [TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)]
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another")
        ]
        actual = split_nodes_link(node)
        self.assertEqual(expected, actual)

    # TEST text_to_textnodes
    
    def test_text_to_textnodes_given_valid_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_text_to_textnodes_given_invalid_bold(self):
        text = "This is **text* with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertRaises(Exception, text_to_textnodes, text)
    
    def test_text_to_textnodes_given_invalid_italic(self):
        text = "This is **text** with an italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertRaises(Exception, text_to_textnodes, text)
    
    def test_text_to_textnodes_given_invalid_code(self):
        text = "This is **text** with an *italic* word and a `code block and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertRaises(Exception, text_to_textnodes, text)