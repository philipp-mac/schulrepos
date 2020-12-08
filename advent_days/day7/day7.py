with open("day7input.md") as source:
    data = source.read()
data = data.split("\n")
rulesArr = [rule.split(" ") for rule in data]

def start(i):
    return (" ").join(rulesArr[i][:2])

def end(i):
    return (" ").join(rulesArr[i][4:])

def part1(rules):
    containerList = []
    for i in range(len(rules)):
        if "shiny gold" in end(i):
            containerList.append(start(i))

    loopThroughAllNested = True
    while loopThroughAllNested:
        loopThroughAllNested = False
        for n in range(0, len(containerList)):
            for k in range(len(rules)):
                if containerList[n] in end(k) and start(k) not in containerList:
                    containerList.append(start(k))
                    loopThroughAllNested = True
    return len(containerList)

def parseContents(string):
    toParse = string.split(" ")
    returnDict = {}
    for i in range(len(toParse)):
        if toParse[i].isnumeric():
            returnDict.update({(" ").join(toParse[i + 1: i + 3]) : int(toParse[i])})
    return returnDict


def ruleDict(rules):
    result = {}
    for i in range(len(rules)):
        result.update({start(i) : parseContents(end(i))})
    return result

def part2(rules):
    # bagRules = dict of dict of all bags, eg:
    # {'shiny gold : {'pale maroon': 2, 'pale purple': 5, 'posh brown': 4, 'dotted turquoise': 1}, ...}
    bagRules = ruleDict(rules)
    def rec(bagName, howOften):
        return sum(
            rec(key, value * howOften) for key, value in bagRules[bagName].items()) + howOften

    return rec('shiny gold', 1) - 1 # minus outer bag


print(part1(rulesArr))
print(part2(rulesArr))