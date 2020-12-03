from day3input import route
route = list(filter(bool, route.split("\n")))

def traverseRouteAndCountTrees(x, y, route):
    treesEncountered = 0
    currentx = 0
    currenty = 0
    for row in range(0, len(route), y):
        treesEncountered += (route[row][currentx % len(route[0])] == "#")
        currentx += x
    return treesEncountered

print("for right 1, down 1: ",traverseRouteAndCountTrees(1, 1, route))
print("for right 3, down 1: ",traverseRouteAndCountTrees(3, 1, route))
print("for right 5, down 1: ",traverseRouteAndCountTrees(5, 1, route))
print("for right 7, down 1: ",traverseRouteAndCountTrees(7, 1, route))
print("for right 1, down 2: ",traverseRouteAndCountTrees(1, 2, route))
print(traverseRouteAndCountTrees(1, 1, route) *
traverseRouteAndCountTrees(3, 1, route) *
traverseRouteAndCountTrees(5, 1, route) *
traverseRouteAndCountTrees(7, 1, route) *
traverseRouteAndCountTrees(1, 2, route))

