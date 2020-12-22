import re, itertools, copy
with open("day14input.md") as source:
    data = source.read()

data = [line for line in data.split("\n") if line != ""]
mem = {}


def bitsToListOfMaskLength(mask, bits):
    if len(mask) > len(bits):
        return list(bits.rjust(len(mask), "0"))
    else:
        return list(bits)


def applyMask(mask, bits):
    bits = bitsToListOfMaskLength(mask, bits)
    for bit in range(len(mask)):
        if mask[bit] != "X":
            bits[bit] = mask[bit]
    return "".join(bits)


def setBitsAndFloating(mask, bits):
    bits = bitsToListOfMaskLength(mask, bits)
    for bit in range(len(mask)):
        if mask[bit] == "1" or mask[bit] == "X":
            bits[bit] = mask[bit]
    return "".join(bits)


def assembleFromCombination(address, floatingBits):
    count = 0
    tempAddr = list(copy.deepcopy(address))
    for bit in range(len(address)):
        if tempAddr[bit] == "X":
            tempAddr[bit] = str(floatingBits[count])
            count += 1
        if count == len(floatingBits):
            break
    return "".join(tempAddr)


def findMemoryLocations(mask, address):
    address = setBitsAndFloating(mask, address)

    n = list(mask).count("X")
    combinations = list(itertools.product([0, 1], repeat=n))

    allAddresses = []
    for floatingBits in combinations:
        allAddresses.append(assembleFromCombination(address, floatingBits))
        
    return allAddresses


def setMem(addresses, bits, mem):
    for a in addresses:
        mem[int(a, base=2)] = int(bits, base=2)
    return mem


def run(data:list, mem:dict, part1:bool):
    print("~~~~~~~~~~~~~~~~~~~~~")
    for line in data:
        if "mask" in line:
            bitMask = line[7:]
        else:
            # these two lines do a regex search for everything inside square brackets
            strAdress = re.search("\[(.*?)\]", line).group(0)
            # and then cast the result of that search to an int (removing the square brackets)
            memAdress = int(strAdress[1:len(strAdress) - 1]) 
            # search for everything after "= " and then cast it to a binary number as a string (Cuts of "0b" at the start)
            bits = bin(int(re.search("\= (.*)", line).group(0)[2:]))[2:]

            #self-explanatory
            if part1:
                mem[memAdress] = int(applyMask(bitMask, bits), base=2)

            else:
                mem = setMem(findMemoryLocations(bitMask, bin(memAdress)[2:]), bits, mem)


def tally(mem:dict):
    totalInMem = 0
    for address in mem:
        totalInMem += mem[address]
    print(totalInMem)

run(data, mem, part1=False)
tally(mem)