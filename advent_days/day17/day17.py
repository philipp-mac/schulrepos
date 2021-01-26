import copy

with open("day17.md") as source:
    data = [item.strip() for item in source.readlines()]

def cycle(board, numOfCycles):
    for c in range(numOfCycles):
        boardCopy = copy.deepcopy(board)
        for row in range(len(board)):
            for item in range(len(board[row])):
                if board[row][item] == ".":
                    status = "inactive"
                else:
                    status = "active"
                for positionAdjacent in range(-1, 1, 1):
                    nearbyArr = []
                    try:
                        nearbyArr.append(board[row + positionAdjacent])
                    except IndexError:
                        continue
                boardCopy[row][item] = getNextState(status, nearbyArr)
        board = copy.deepcopy(boardCopy)
    return board

def getNextState(status, nearby):
    return 0

print(cycle(data, 6))