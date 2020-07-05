import unittest
from seoanalyzer.parser import HTMLParser


class MyTestCase(unittest.TestCase):
    def test_read(self):
        self.assertIsNotNone(HTMLParser.read("../testFiles/test1.html"))


if __name__ == '__main__':
    unittest.main()
