"""
Analyzer class responsibility to bridge the html tage validate against the rule set.
Implementation related to HTML iterator and use evaluator to validate against rules
"""

from seoanalyzer.parserEx import HTMLParserEx
from seoanalyzer.ruleParser import RuleParser
from seoanalyzer.evaluator import Evaluator


class Analyzer:
    rule_json = {}

    @staticmethod
    def load_rules(path):
        Analyzer.rule_json = RuleParser.parse(path)

    def __init__(self, rule_file=None):
        if rule_file is not None:
            Analyzer.load_rules(rule_file)

    def analyze(self, html="", html_file=None, print_errors=True):
        if not self.rule_json:
            raise AssertionError("rule file not loaded")
        data = None
        if html_file is not None:
            with open(html_file, "r") as f:
                data = f.read()

        if data is None:
            data = html
        errors = []
        parser = HTMLParserEx()
        root = parser.feed(data)
        parser.close()
        # print(self.rule_json)
        for tag, rule in self.rule_json.items():
            if rule == "required":
                err = Evaluator.evaluate_required_tags(root, tag, rule)
                if err is not None:
                    errors.append(err)
            elif isinstance(rule, list):
                err = Evaluator.evaluate_attributes(root, tag, rule)
                if err is not None:
                    errors.append(err)
            elif isinstance(rule, int):
                err = Evaluator.evaluate_tag_count(root, tag, rule)
                if err is not None:
                    errors.append(err)

        if print_errors:
            for err in errors:
                print(err)
        else:
            return errors

# seoanalyzer = Analyzer(rule_file="../rules/simplified_rules.json")
# # seoanalyzer.load_rules("../rules/simplified_rules.json")
# # # seoanalyzer.analyze('<img src="python-logo.png"> <a def="" /a><img src="python-logo.png">')
# seoanalyzer.analyze(html_file="../testFiles/test1.html")
