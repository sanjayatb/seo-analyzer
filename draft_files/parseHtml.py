from html.parser import HTMLParser
from html.entities import name2codepoint
import json
import copy

class MyHTMLParser(HTMLParser):
    ruleJson = []
    with open("rules.json") as f:
        ruleJson = json.load(f)
    rules = copy.deepcopy(ruleJson)
    errors = []
    print(rules)
    tagStack = []
    scope = []
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        if tag not in self.rules:
            return
        rule = copy.deepcopy(self.rules[tag])
        print(rule)

        if 'withoutTag' in rule:
            self.scope.append(tag)
            for tag in self.rules[tag]['withoutTag']:
                self.tagStack.append(tag)

        if 'maxTagCount' in rule:
            rule['maxTagCount'] -= 1
            self.rules[tag] = rule

        for attr in attrs:
            if 'without' in rule:
                rule['without'].remove(attr[0])

        if 'without' in rule:
            if rule['without']:
              self.errors.append(tag)
        if 'maxTagCount' in rule:
            if rule['maxTagCount'] < 0:
                self.errors.append(tag)
            print(tag+" : "+str(rule['maxTagCount']))

    def handle_endtag(self, tag):
        print("End tag  :", tag)
        print("Tag stack :", self.tagStack)
        print("scope stack :", self.scope)
        if self.scope:
            print("removed scope: " + self.scope.pop())
        if tag in self.tagStack:
            print("removed : "+self.tagStack.pop())

    # def handle_data(self, data):
    #     print("Data     :", data)
    def get_errors(self):
        withoutError = "There are {0} <{1}> tag without {2} attributes"
        ferq = {}
        for error in self.errors:
            if error in ferq:
                ferq[error] += 1
            else:
                ferq[error] = 1
        errStr = []
        for tag,cnt in ferq.items():
            if self.tagStack:
                errStr.append(tag + " tag is not there in ")
            if "errorStr" in self.rules[tag]:
                errStr.append(self.rules[tag]['errorStr'].format(self.ruleJson[tag]['maxTagCount']))
            else:
                err = withoutError.format(cnt,tag,self.rules[tag]["without"])
                errStr.append(err)
        return errStr

file = open("../testFiles/test1.html", "r")
parser = MyHTMLParser()
# parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')
# parser.feed('<img src="python-logo.png"> <a def="" /a><img src="python-logo.png">')
parser.feed(file.read())

for err in parser.get_errors():
    print(err)