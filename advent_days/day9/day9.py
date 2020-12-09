example_input = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''

with open("day9input.md") as source:
    data = source.read()
data = data.split("\n")
data = [int(item) for item in data if item.isnumeric()]


example_input = example_input.split("\n")
example_input = [int(item) for item in example_input if item.isnumeric()]

def calcValid(preamble):
    result = []
    for item in range(len(preamble)):
        for otherItem in range(len(preamble)):
            if preamble[otherItem] != preamble[item]:
                result.append(preamble[item] + preamble[otherItem])
    return result

def validated(item, validList):
    if item not in validList:
        return False
    else:
        return True

def part2(nums, soughtIndex):
    for i in range(len(nums)):
        delimiter = 1
        while (delimiter < 50):
            print(delimiter, " in while")
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
    for i in range(preambleLen, len(nums)):
        if not validated(nums[i], calcValid(nums[i - preambleLen: i])):
            if secondPart:
                return part2(nums, i)
            return nums[i]

print(solve(data, 25))