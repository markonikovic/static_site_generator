from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test.__repr__())
    test2 = HTMLNode("h1", "This is a heading level 1",
                     None, {"color": "blue"})
    print(test2.__repr__())

    test3 = LeafNode("h1", "This is an epic test", {"href": "https://www.marko.com", "color": "blue"})
    print(test3.to_html())


main()
