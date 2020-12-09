import re

with open("day2input.md") as source:
    policiesAndPasswords = source.readlines()
policiesAndPasswords = [item.strip() for item in policiesAndPasswords]
policiesAndPasswords = [item.split(":") for item in policiesAndPasswords]

def passwordIsValid(policy, password):
    conditionList = re.split('[- ]', policy)
    minOcc = int(conditionList[0])
    maxOcc = int(conditionList[1])
    wantedChar = conditionList[2]
    return password.count(wantedChar) >= minOcc and password.count(wantedChar) <= maxOcc

def passwordIsValidPartTwo(policy, password):
    conditionList = re.split('[- ]', policy)
    indexOne = int(conditionList[0])
    indexTwo = int(conditionList[1])
    wantedChar = conditionList[2]
    return bool(password[indexOne] == wantedChar) != bool(password[indexTwo] == wantedChar)

def checkRecords(list): 
    global validPasswords
    for i in range(len(list)):
        # if passwordIsValid(list[i][0], list[i][1]):
        #     validPasswords += 1
        if passwordIsValidPartTwo(list[i][0], list[i][1]):
            validPasswords += 1

validPasswords = 0
checkRecords(policiesAndPasswords)
print(validPasswords)