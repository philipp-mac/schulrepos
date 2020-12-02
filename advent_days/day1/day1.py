with open("day1input.md") as source:
    expenses = source.readlines()
expenses = [item.strip() for item in expenses] 
expenses = [int(item) for item in expenses]

def swap(list, a, b):
    temp = list[b]
    list[b] = list[a]
    list[a] = temp

def bubbleSort(list):
    keepGoing = True
    while keepGoing:
        keepGoing = False
        for n in range(1, len(list)):
            if list[n] < list [n - 1]:
                swap(list, n, n-1)
                keepGoing = True

def findTwo(list, targetNum):
    for num in range(0, len(list)):
        needed =  2020 - list[num]
        print(list[num], needed)
        if needed in list[num+1:]:
            return list[num], list[list.index(needed)]

def findThree(list, targetNum):
    pass
            

bubbleSort(expenses)
result = findTwo(expenses, 2020)
print(result[0] * result[1])

resultPart2 = findThree(expenses, 2020)
print()