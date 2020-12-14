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
    if direction == 'R':
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
    directions = {"E" : (0, 1), "W": (0, -1),
                "N": (1, 0), "S": (-1, 0)}

    for move in moves:
        print(move, " , current Pos is ", currentPos, " facing ", facing)
        if move[0] == "L" or move[0] == "R":
            facing = getNewFacing(facing, move[0], move[1])
        if move[0] == "F":
            currentPos[0] += directions[facing][0] * move[1]
            currentPos[1] += directions[facing][1] * move[1]
        elif move[0] in directions.keys():
            currentPos[0] += directions[move[0]][0] * move[1]
            currentPos[1] += directions[move[0]][1] * move[1]
        print("facing ", facing, " after move at ", currentPos, "\n -------------")


    return abs(currentPos[0]) + abs(currentPos[1])

print("__________NEW RUN________")
print(moveShip(moves))