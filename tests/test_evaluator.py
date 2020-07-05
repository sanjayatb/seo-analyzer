import unittest
from seoanalyzer.parserEx import HTMLParserEx
from seoanalyzer.evaluator import Evaluator


class EvaluatorTest(unittest.TestCase):
    parser = HTMLParserEx()

    def test_evaluate_required_tags_error(self):
        data = "<html></html>"
        html = self.parser.feed(data)
        self.assertEqual("This HTML not having <title> tag", Evaluator.evaluate_required_tags(html, "title", "required"))

    def test_evaluate_required_tags(self):
        data = "<html><title/></html>"
        html = self.parser.feed(data)
        self.assertEqual(None, Evaluator.evaluate_required_tags(html, "title", "required"))

    def test_evaluate_attributes_error(self):
        data = "<html><img /></html>"
        html = self.parser.feed(data)
        self.assertEqual("There are 1 <img> tag without alt attributes", Evaluator.evaluate_attributes(html, "img", ["alt"]))

    def test_evaluate_required_tags(self):
        data = "<html><img alt=\"test\"/></html>"
        html = self.parser.feed(data)
        self.assertEqual(None, Evaluator.evaluate_attributes(html, "img", ["alt"]))

    def test_evaluate_tag_count_error(self):
        data = """<html>
                <strong></strong><strong></strong><strong></strong>
                <strong></strong><strong></strong><strong></strong><strong></strong><strong>
                </strong><strong></strong><strong></strong><strong></strong><strong></strong><strong></strong>
                </html>
               """
        html = self.parser.feed(data)
        self.assertEqual("This HTML having more than 10 <strong> tag", Evaluator.evaluate_tag_count(html, "strong", 10))

    def test_evaluate_tag_count(self):
        data = """<html>
                    <strong></strong><strong></strong><strong></strong>
                    </html>
                """
        html = self.parser.feed(data)
        self.assertEqual(None, Evaluator.evaluate_tag_count(html, "strong", 5))


if __name__ == '__main__':
    unittest.main()
