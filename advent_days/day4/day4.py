import re, copy

with open("day4input.md") as source:
    batch = source.read()
batch = batch.split("\n\n")
batch = [re.split("[:\n ]", item) for item in batch]


def countValidPassports(batch, requiredFields, part):
    validPassports = 0
    for passport in batch:
        fieldsMatchedAndValid = 0
        for item in range(len(passport)):
            if passport[item] in requiredFields:
                if part == 1:
                    fieldsMatchedAndValid += 1
                else:
                    ##item is the category, item + 1 is the actual content for part 2
                    if validateContent(passport[item], passport[item + 1]):
                        fieldsMatchedAndValid += 1
        if fieldsMatchedAndValid >= 7:
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
    fieldCopy = copy.deepcopy(field)
    if len(fieldCopy) < 4:
        return False
    unit = field[len(field) - 2:]
    number = int(field[0:len(field) - 2])
    if unit == "cm":
        return number >= 150 and number <= 193
    elif unit == "in":
        return number >= 59 and number <= 76
    else: 
        return False

def validHcl(field):
    print(field)
    print(re.match("^[#][0-9a-f]{6}", field))
    return re.match("^[#][0-9a-f]{6}", field)

def validEcl(field):
    return re.match("[amb|blu|brn|gry|grn|hzl|oth]{3}", field) and len(field) == 3

def validPid(field):
    return field.isnumeric() and len(field) == 9

print(countValidPassports(batch, ["byr","iyr","eyr","hgt","hcl","ecl","pid"], 1))
# print(countValidPassports(batch, ["byr","iyr","eyr","hgt","hcl","ecl","pid"], 2))