with open("day13input.md") as source:
    data = source.read()

data = data.split("\n")
maxWait = int(data[0])
lines = data[1].split(",")

buslines = [int(item) for item in lines if item.isnumeric()]
buslines2 = [item for item in lines]

def getDepartures(buslines):
    departureDict = {}
    for bus in buslines:
        departureDict[bus] = []
        currentDeparture = 0
        while currentDeparture <= maxWait + bus:
            departureDict[bus].append(currentDeparture)
            currentDeparture += bus
    return departureDict


def getClosest(maxWait, departureDict):
    closestAndID = [maxWait + min(list(departureDict.keys())), 0]
    for bus in list(departureDict.keys()):
        for time in departureDict[bus]:
            if time > maxWait and time < closestAndID[0]:
                closestAndID[0] = time
                closestAndID[1] = bus
    return (closestAndID[0] - maxWait) * closestAndID[1]   # part 1          


def getCorrectOffsets(buslines):
    offsets = []
    lastValid = 0
    for bus in range(len(buslines)):
        pass
        


# print(getClosest(maxWait, getDepartures(buslines)))