Python SEO Analyzer
===================

An SEO analyzer tool that analyzes the structure of a html page, based on configurable SEO rules.

Requires Python 3.7+

Installation
------------

### PIP

```
pip3 install seo-analyzer
```

Command-line Usage
------------------
If you run on a given HTML file.

```sh
seoanalyze path/to/file.html
```

If you run on a given URL of a web page.

```sh
seoanalyze http://www.domain.com/
```

API
---

The `analyze` function returns a list of errors.

```python
from seoanalyzer.htmlAnalyzer import Analyzer

analyzer = Analyzer(rule_file="rules/simplified_rules.json")
output = analyzer.analyze(html_file="testFiles/test1.html")

print(output)
```

Notes
-----