class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node, node2):
        if node.text == node2.text and node.text_type == node2.text_type and node.url == node2.url:
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
