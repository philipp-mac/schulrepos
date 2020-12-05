import math

with open("day5input.md") as source:
    data = source.read()
data = data.split("\n")


def getSeatsAndLimit(data):
    seatIDs = []
    for bPass in data:
        rowCode = bPass[:7]
        colCode = bPass[len(bPass) -3:]
        seatIDs.append(calcRow(rowCode) * 8 + calcCol(colCode))
    findMissingSeat(seatIDs)
    return max(seatIDs)

def calcRow(code):
    minSeatNum = 0
    maxSeatNum = 127
    for letter in range(len(code)):
        if code[letter] == "B":
            minSeatNum = math.ceil(minSeatNum + (maxSeatNum - minSeatNum) / 2)
        elif code[letter] == "F":
            maxSeatNum = math.floor(maxSeatNum - (maxSeatNum - minSeatNum) / 2)
    return maxSeatNum #both numbers are equal at the end, could return either one

def calcCol(code):
    minSeatNum = 0
    maxSeatNum = 7
    for letter in range(len(code)):
        if code[letter] == "R":
            minSeatNum = math.ceil(minSeatNum + (maxSeatNum - minSeatNum) / 2)
        elif code[letter] == "L":
            maxSeatNum = math.floor(maxSeatNum - (maxSeatNum - minSeatNum) / 2)
    return maxSeatNum #both numbers are equal at the end, could return either one

def findMissingSeat(idList):
    bubbleSort(idList)
    for n in range(1, len(idList)):
        step = idList[n] - idList[n - 1]
        if step != 1:
            print("Seat between ", idList[n], " and ", idList[n - 1], " is missing.")

def swap(arr, indexA, indexB):
    temp = arr[indexB]
    arr[indexB] = arr[indexA]
    arr[indexA] = temp

def bubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if (array[i] < array[i - 1]):
                swap(array, i, i - 1)
                swapped = True 



print("Highest Seat ID is: ", getSeatsAndLimit(data))