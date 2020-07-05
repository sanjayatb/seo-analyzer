import unittest
from draft_files.validator import Validator


class ValidatorTest(unittest.TestCase):
    validator = Validator()

    def test_validate_attributes(self):
        self.assertEqual(None, self.validator.validate_attributes("img", [("alt", "text")]))

    def test_validate_attributes_error(self):
        self.assertEqual('img', self.validator.validate_attributes("img", []))

    def test_validate_tag_count(self):
        self.assertEqual(None, self.validator.validate_tag_count("h1"))

    def test_validate_tag_count_error(self):
        for i in range(15): # tag found 15 times
            self.validator.validate_tag_count("strong")
        self.assertEqual('strong', self.validator.validate_tag_count("strong"))


if __name__ == '__main__':
    unittest.main()
