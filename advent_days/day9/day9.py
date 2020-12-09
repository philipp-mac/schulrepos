with open("day9input.md") as source:
    data = source.read()
data = data.split("\n")
data = [int(item) for item in data if item.isnumeric()]

def calcValid(preamble):
    result = []
    for item in range(len(preamble)):
        for otherItem in range(len(preamble)):
            if preamble[otherItem] != preamble[item]:
                result.append(preamble[item] + preamble[otherItem])
    return result

def validated(item, validList):
    return item in validList

def part2(nums, soughtIndex):
    for i in range(len(nums)):
        delimiter = 1
        while (delimiter < 50):
            preamble = nums[i: i + delimiter]
            attempt = sum(preamble)
            if nums[soughtIndex] == attempt:
                print("solved part 2")
                return min(preamble) + max(preamble)
            elif attempt > nums[soughtIndex]:
                delimiter = 1
                break
            elif attempt < nums[soughtIndex]:
                delimiter += 1


def solve(nums, preambleLen):
    secondPart = True
    ##part1
    for i in range(preambleLen, len(nums)):
        if not validated(nums[i], calcValid(nums[i - preambleLen: i])):
            ##part2 return
            if secondPart:
                return part2(nums, i)
            ##part 1 return
            return nums[i]

print(solve(data, 25))