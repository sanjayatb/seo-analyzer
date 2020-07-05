"""
Evaluator is a utility class for evaluate SEO rules on the HTML given
Use can add customizable rule evaluations here, without changing the main code
"""

attribute_error = "There are {0} <{1}> tag without {2} attributes"
tag_error = "This HTML not having <{0}> tag"
tag_child_attr_error = "This HTML doesn't have <{0} {1}> tag"
tag_count_error = "This HTML having more than {0} <{1}> tag"


class Evaluator:

    @staticmethod
    def evaluate_required_tags(html_root, tag, rule):
        if rule != "required":
            raise AssertionError("This method not supported for given rule")
        if html_root.find(tag) is None:
            return tag_error.format(tag)

    @staticmethod
    def evaluate_attributes(html_root, tag, rule):
        for ruleTag in rule:
            count = 0
            required_tag = 0
            reg_attr_flag = False
            for attrs in html_root.findall('.//' + tag):
                _extracted = ruleTag.split('=')
                _data = attrs.get(_extracted[0])
                if len(_extracted) == 1:
                    if not _data:
                        count += 1
                else:
                    reg_attr_flag = True
                    if _extracted[1] == _data:
                        required_tag += 1

            if count > 0:
                return attribute_error.format(count, tag, ruleTag)
            elif reg_attr_flag and required_tag == 0:
                return tag_child_attr_error.format(tag, ruleTag)

    @staticmethod
    def evaluate_tag_count(html_root, tag, rule):
        count = int(rule)
        for attrs in html_root.findall('.//' + tag):
            count -= 1
        if count < 0:
            return tag_count_error.format(int(rule), tag)

