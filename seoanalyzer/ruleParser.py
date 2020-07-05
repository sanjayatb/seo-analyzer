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