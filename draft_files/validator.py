#!/usr/bin/env python
"""
Validator class is the bridge between loaded rules validate against the htnl
"""

import json
import copy


class Validator:
    with open("rules.json") as f:
        ruleJson = json.load(f)
    rules = copy.deepcopy(ruleJson)
    errors = []

    def validate_attributes(self, tag, attrs):
        if tag not in self.rules:
            return
        rule = copy.deepcopy(self.rules[tag])
        rule_key = "without"

        if rule_key not in rule:
            raise BaseException("This tag is not related to attribute check")

        for attr in attrs:
            rule[rule_key].remove(attr[0])
        if rule[rule_key]:
            return tag
        return None

    def validate_tag_count(self, tag):
        if tag not in self.rules:
            return
        rule = copy.deepcopy(self.rules[tag])
        rule_key = "maxTagCount"

        if rule_key not in rule:
            raise BaseException("This tag is not related to tag count check")

        rule[rule_key] -= 1
        self.rules[tag] = rule

        if rule[rule_key] < 0:
            return tag
        return None
