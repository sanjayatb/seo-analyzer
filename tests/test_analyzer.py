import unittest
from seoanalyzer.htmlAnalyzer import Analyzer


class AnalyzerTestCase(unittest.TestCase):
    def test_rule_not_load(self):
        analyzer = Analyzer()
        self.assertRaises(AssertionError, analyzer.analyze, "html data")

    def test_analyze(self):
        analyzer = Analyzer("../rules/simplified_rules.json")
        self.assertEqual(None, analyzer.analyze(html="<html></html>"))


if __name__ == '__main__':
    unittest.main()
