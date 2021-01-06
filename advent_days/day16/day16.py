from collections import defaultdict
import re

# rules = defaultdict()
tickets = []

def parseLine(line, mode):
    ## specific rules parser, may be needed later 
    # if mode == "rule":
    #     rule = re.search("^[^:]+", line).group(0)
    #     ranges = re.search("[^:]+$", line).group(0).strip()
    #     rules[rule] = ranges
    #     print(rules[rule]) 

    if mode == "rule":
        validRanges.append([int(n) for n in re.findall(r'\b\d+\b', line)])

    if mode == "myTicket" or mode == "otherTickets":
        numbers = [int(n) for n in line.split(",") if n.strip().isnumeric()]
        if numbers != []:
            tickets.append(numbers)

def readValidRangesFromInput():
    global validRanges
    validRanges = []
    with open("day16input.md") as source:
        modes = {0: "rule", 1: "myTicket", 2: "otherTickets"}
        mode = 0
        for line in source:
            if len(line) == 1:  
                mode += 1
            parseLine(line, modes[mode])
    return validRanges


def formatValidRanges(validRanges):
    formattedRanges = []
    for rng in validRanges:
        formattedRanges.append([[rng[0], rng[1]], [rng[2], rng[3]]])
    return formattedRanges

def valid(value):
    for ranges in validRanges:
        for rng in ranges:
            if value > rng[0] and value < rng[1]:
                return True
    return False

def getInvalidAllRules(tickets):
    invalidFields = []
    for ticket in tickets:
        for value in ticket:
            if not valid(value):
                invalidFields.append(value)
    return invalidFields

def calcScanningError(invalidFields):
    result = 0
    for item in invalidFields:
        result += item
    return result

validRanges = readValidRangesFromInput()
validRanges = formatValidRanges(validRanges)
invalidFields = getInvalidAllRules(tickets)
print(calcScanningError(invalidFields))