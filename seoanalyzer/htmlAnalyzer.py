from seoanalyzer.parserEx import HTMLParserEx
from seoanalyzer.ruleParser import RuleParser

attribute_error = "There are {0} <{1}> tag without {2} attributes"
tag_error = "This HTML not having <{0}> tag"
tag_child_attr_error = "This HTML doesn't have <{0} {1}> tag"
tag_count_error = "This HTML having more than {0} <{1}> tag"


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
                if root.find(tag) is None:
                    errors.append(tag_error.format(tag))
            elif isinstance(rule, list):
                for ruleTag in rule:
                    count = 0
                    required_tag = 0
                    for attrs in root.findall('.//'+tag):
                        _extracted = ruleTag.split('=')
                        _data = attrs.get(_extracted[0])
                        if len(_extracted) > 1:
                            if _extracted[1] == _data:
                                required_tag += 1
                        else:
                            if not _data:
                                count += 1
                    if count > 0:
                        errors.append(attribute_error.format(count, tag, ruleTag))
                    if count == 0 and required_tag == 0:
                        errors.append(tag_child_attr_error.format(tag, ruleTag))

            elif isinstance(rule, int):
                count = int(rule)
                for attrs in root.findall('.//' + tag):
                    count -= 1
                if count < 0:
                    errors.append(tag_count_error.format(int(rule), tag))

        if print_errors:
            for err in errors:
                print(err)
        else:
            return errors

# seoanalyzer = Analyzer(rule_file="../rules/simplified_rules.json")
# # seoanalyzer.load_rules("../rules/simplified_rules.json")
# # seoanalyzer.analyze('<img src="python-logo.png"> <a def="" /a><img src="python-logo.png">')
# seoanalyzer.analyze(html_file="../testFiles/test1.html")
