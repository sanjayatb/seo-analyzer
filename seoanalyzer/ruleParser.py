#!/usr/bin/env python
"""
RuleParser is a class where user can customize rules in user friendly way.
Seperation of rule parsing from main logic, make it easy to change when rules are evolving.
"""

import json
import re

required_regex = "required"
without_attr_regex = "without {(\w+)} attribute"
tag_count_regex = "more than {(\d+)} tags"
tag_key_value_regex = "(\w+)=(\w+)"

txt_no = "(\d+)."
txt_attr_regex = txt_no+" {<(\w+) />} tag without {(\w+)} attribute"
txt_does_not_have = txt_no+" {<(\w+)>} tag doesn't have {(\w+)} tag"
txt_tag_count = txt_no+" {<(\w+))>} tag appears more than {(\d+))} times"

class RuleParser:

    @staticmethod
    def parse(file_path):
        parsed_json = {}
        with open(file_path) as f:
            rule_json = json.load(f)
        for tag, rule in rule_json.items():
            if isinstance(rule, list):
                for tagContent in rule:
                    tag_key_value_reg = re.search(tag_key_value_regex, tagContent)
                    if tag_key_value_reg is not None:
                        parsed_json[tag] = rule

            elif isinstance(rule, str):
                if re.search(required_regex, rule) is not None:
                    parsed_json[tag] = rule
                attr_reg = re.search(without_attr_regex, rule)
                if attr_reg is not None:
                    parsed_json[tag] = list(attr_reg.groups())
                tag_cnt_reg = re.search(tag_count_regex, rule)
                if tag_cnt_reg is not None:
                    parsed_json[tag] = int(tag_cnt_reg.groups()[0])
            # print(parsed_json)
        return parsed_json

    #### This method can be used to parse rule those are in the form in text lines
    # TODO optimize regex search and build the rule
    @staticmethod
    def parse_expr_rule(file_path):
        rule_book = []
        with open(file_path) as file:
            rule_txt = file.read()

        rule_set = rule_txt.split("\n")
        for rule in rule_set:
            params = re.match(txt_attr_regex, rule)
            made_up_rule = {}
            if params is not None:
                made_up_rule[params[2]] = [params[3]]
                rule_book.append(made_up_rule)
                print(params.groups())
            else:
                params = re.match(txt_does_not_have, rule)
                if params is not None:
                    print(params.groups())
                else:
                    params = re.search(txt_tag_count, rule)
                    print(params.groups())
        print(rule_set)
        print(rule_book)

### Using regular expresion, we can simplyfy the seo rules
# TODO  create parsed rule set using a text file and feed to the analyzer
# TODO create numbered rule set and use them as a to enable/disable rules
# RuleParser.parse_expr_rule("../rules/rule_book.txt")