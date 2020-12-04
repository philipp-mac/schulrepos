import re

with open("day4input.md") as source:
    batch = source.read()
batch = batch.split("\n\n")
batch = [re.split("[:\n ]", item) for item in batch]


def countValidPartOne(batch, requiredFields):
    validPassports = 0
    for passport in batch:
        fieldsMatched = 0
        validatedFields = 0
        for item in passport:
            if item in requiredFields:
                fieldsMatched += 1
        if fieldsMatched >= 7:
            validPassports += 1
    return validPassports


def countValidPartTwo(batch, requiredFields):
    validPassports = 0
    for passport in batch:
        fieldsMatchedAndValid = 0
        validatedFields = 0
        for item in range(len(passport)):
            if passport[item] in requiredFields:
                if validateContent(passport[item], passport[item + 1]):
                    validatedFields += 1
                if validatedFields >= 7:
                    validPassports += 1
    return validPassports


def validateContent(field, content):
    if field == "byr":
        return validByr(content)
    elif field == "iyr":
        return validIyr(content)
    elif field == "eyr":
        return validEyr(content)      
    elif field == "hgt":
        return validHgt(content)
    elif field == "hcl":
        return validHcl(content)
    elif field == "ecl":
        return validEcl(content)
    elif field == "pid":
        return validPid(content)
            


def validByr(field):
    return len(field) == 4 and int(field) <= 2002 and int(field) >= 1920

def validIyr(field):
    return len(field) == 4 and int(field) <= 2020 and int(field) >= 2010

def validEyr(field):
    return len(field) == 4 and int(field) <= 2030 and int(field) >= 2020

def validHgt(field):
    if len(field) < 4 or len(field) > 6:
        return False
    unit = field[len(field) - 2:]
    number = int(field[0:len(field) - 2])
    if unit == "cm":
        return number >= 150 and number <= 193
    elif unit == "in":
        return number >= 59 and number <= 76
    else: 
        return False

#check
def validHcl(field):
    return re.match("^[#][0-9a-f]{6}", field)

#check
def validEcl(field):
    return re.match("[amb|blu|brn|gry|grn|hzl|oth]{3}", field) != None and len(field) == 3

def validPid(field):
    return field.isnumeric() and len(field) == 9

# print(countValidPassports(batch, ["byr","iyr","eyr","hgt","hcl","ecl","pid"], 1))
result  = countValidPartTwo(batch, ["byr","iyr","eyr","hgt","hcl","ecl","pid"]) - 1 #einen drüber
print(result)