import unittest
from seoanalyzer.parserEx import HTMLParserEx


class ParserTestCase(unittest.TestCase):
    def test_feed(self):
        parser = HTMLParserEx()
        self.assertIsNotNone(parser.feed("<html><html/>"))


if __name__ == '__main__':
    unittest.main()
