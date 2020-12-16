import copy, math

with open("day12input.md") as source:
    moves = source.read()
moves = moves.split("\n")

def prepareInput(moves):
    moveList = [[]]*len(moves)
    for j in range(len(moves)):
        for i in range(len(moves[j])):
            if moves[j][i].isnumeric():
                moveList[j] = [moves[j][:i], int(moves[j][i:len(moves[j])])]
                break
    return moveList

moves = prepareInput(moves)
##############

def getNewFacing(facing, direction, degrees):
    angles = {"N": 0, "E": 90, "S": 180, "W": 270}

    if direction == 'L':
        angle = angles[facing]
        degreesLeft = degrees
        while True:
            angle -= 90
            if angle < 0:
                angle = 270
            degreesLeft -= 90
            if degreesLeft == 0:
                break
        return list(angles.keys())[list(angles.values()).index(angle)]
        
    elif direction == 'R':
        angle = angles[facing]
        degreesLeft = degrees
        while True:
            angle += 90
            if angle == 360:
                angle = 0
            degreesLeft -= 90
            if degreesLeft == 0:
                break
        return list(angles.keys())[list(angles.values()).index(angle)]

        
def moveShip(moves):
    #move[0] = direction, move[1] = value
    currentPos = [0, 0]
    facing = "E"
    directions = {"E" : (1, 0), "W": (-1, 0),
                "N": (0, 1), "S": (0, -1)}

    for move in moves:
        if move[0] == "L" or move[0] == "R":
            facing = getNewFacing(facing, move[0], move[1])
        if move[0] == "F":
            currentPos[0] += directions[facing][0] * move[1]
            currentPos[1] += directions[facing][1] * move[1]
        elif move[0] in directions.keys():
            currentPos[0] += directions[move[0]][0] * move[1]
            currentPos[1] += directions[move[0]][1] * move[1]

    return abs(currentPos[0]) + abs(currentPos[1])


def rotateWaypoint(waypointPos, direction, degrees):
    newWaypointPos = copy.deepcopy(waypointPos)
    x = waypointPos[0]
    y = waypointPos[1]

    if direction == "R":
        radians = (-degrees) / 180 * math.pi
        newWaypointPos[0] = math.cos(radians) * x - math.sin(radians) * y
        newWaypointPos[1] = math.sin(radians) * x + math.cos(radians) * y

    elif direction == "L":
        radians = degrees / 180 * math.pi
        newWaypointPos[0] = math.cos(radians) * x - math.sin(radians) * y
        newWaypointPos[1] = math.sin(radians) * x + math.cos(radians) * y

    print("radians is ", radians)

    return newWaypointPos


def moveShipViaWaypoint(moves):
    #move[0] = direction, move[1] = value
    currentPos = [0, 0]
    waypointPosRelative = [10, 1]
    facing = "E"
    directions = {"E" : (1, 0), "W": (-1, 0),
                "N": (0, 1), "S": (0, -1)}

    for move in moves:
        print(move, " , current Pos is ", currentPos, " facing ", facing)
        if move[0] == "L" or move[0] == "R":
            waypointPosRelative = rotateWaypoint(waypointPosRelative, move[0], move[1])
        if move[0] == "F":
            for times in range(move[1]):
                currentPos[0] += waypointPosRelative[0]
                currentPos[1] += waypointPosRelative[1]
        elif move[0] in directions.keys():
            waypointPosRelative[0] += directions[move[0]][0] * move[1]
            waypointPosRelative[1] += directions[move[0]][1] * move[1]
        print("facing ", facing, " after move at ", currentPos, " waypoint is at ", waypointPosRelative, "\n -------------")

    return int(abs(currentPos[0]) + abs(currentPos[1]))


print("part1 " , moveShip(moves))
print("part2 " , moveShipViaWaypoint(moves))