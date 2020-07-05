"""
HTMLParser implementation goes here,
Hence this is not the main focus of the library, using existing HTMLParser.
"""


class ParserInterface:

    def __init__(self):
        if self.__class__ is ParserInterface:
            raise RuntimeError("ParserInterface must be subclassed")

    # Overridable -- start tag
    def on_start_tag(self, tag, attributes):
        pass

    # Overridable -- end tag
    def on_end_tag(self, tag, attributes):
        pass

    # Overridable -- scope start tag
    def on_scope_start_tag(self, parent_tag, child_tags):
        pass

    # Overridable -- scope end tag
    def on_scope_end_tag(self, parent_tag, child_tags):
        pass


class HTMLParser(ParserInterface):
    data = ""

    def read(self, file_path):
        with open(file_path, "r") as file:
            self.data = self.data + file.read()

    def parse(self):
        rawdata = self.data
        i = 0
        n = len(rawdata)
        while i < n:
            j = rawdata.find('<', i)
            if j < 0:
                #Simple html parser code goes here
                # Each tag position found, we can call the interface method where use can override
                pass