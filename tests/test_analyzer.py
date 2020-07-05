import unittest
from seoanalyzer.htmlAnalyzer import Analyzer


class MyTestCase(unittest.TestCase):
    def test_rule_not_load(self):
        analyzer = Analyzer()
        self.assertRaises(AssertionError, analyzer.analyze, "html data")


if __name__ == '__main__':
    unittest.main()
