import copy
with open("day11input.md") as source:
    ferry = source.read()

ferry = ferry.split("\n")
ferry = [list(row) for row in ferry]

def iterate(ferry, tolerance, part2):
    print("len of ferry list", len(ferry), "len of ind row", len(ferry[0]))
    while 1:
        result = applyRules(ferry, tolerance, part2)
        newFerry = result[0]
        if result[1] == 0: #means = no changes recorded
            return occupied(ferry)
            break
        ferry = newFerry


def applyRules(ferry, tolerance, part2):
    didChange = 0
    newFerry = copy.deepcopy(ferry)
    for y in range(len(ferry)):
        for x in range(len(ferry[y])):
            if ferry[y][x] == ".":
                continue
            else:
                if part2:
                    criteria = getVisible(y, x, ferry)
                else:
                    criteria = getAdjacent(y, x, ferry)

                if ferry[y][x] == "L" and criteria["occupied"] == 0:
                    newFerry[y][x] = "#"
                    didChange += 1
                elif ferry[y][x] == "#" and criteria["occupied"] >= tolerance:
                    newFerry[y][x] = "L"
                    didChange += 1
    return newFerry, didChange
        
        
def getAdjacent(yRow, xSeat, ferry):
    adj = {"empty" : 0, "occupied": 0}
    directionsYX = [(-1, -1),(-1, 0),(-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]

    for directionYX in directionsYX:
        newY = yRow + directionYX[0]
        newX = xSeat + directionYX[1]

        if (newY >= 0 \
            and newY < len(ferry) \
            and newX >= 0 \
            and newX < len(ferry[0])):
            if ferry[newY][newX] == "#":
                adj["occupied"] += 1
            elif ferry[newY][newX] == "L" or ferry[newY][newX] == ".":
                adj["empty"] += 1
        else:
            adj["empty"] += 1
    return adj


def getVisible(yRow, xSeat, ferry):
    vis = {"empty" : 0, "occupied": 0}
    directionsYX = [(-1, -1),(-1, 0),(-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]
    
    for directionYX in directionsYX:
        newY = yRow + directionYX[0]
        newX = xSeat + directionYX[1]

        while True:
            if (newY >= 0 \
            and newY < len(ferry) \
            and newX >= 0 \
            and newX < len(ferry[0])):
                if ferry[newY][newX] == "#":
                    vis["occupied"] += 1
                    break
                elif ferry[newY][newX] == "L":
                    vis["empty"] += 1
                    break
                elif ferry[newY][newX] == ".":
                    newY = newY + directionYX[0] 
                    newX = newX + directionYX[1]                 
            else:
                vis["empty"] += 1
                break
    return vis


def occupied(ferry):
    count = 0
    for row in ferry:
        for seat in row:
            if seat == "#":
                count += 1
    return count


print("part1: ", iterate(ferry, 4, False))
print("part2: ", iterate(ferry, 5, True))