import re
with open("day14input.md") as source:
    data = source.read()

data = [line for line in data.split("\n") if line != ""]

cache = [0]*700000


def setValuesBitByBit(mask, bits):
    if len(mask) > len(bits):
        bits = list(bits.rjust(len(mask), "0"))
    for bit in range(len(mask)):
        if mask[bit] != "X":
            bits[bit] = mask[bit]
    return "".join(bits)


def run(data, cache):
    for line in data:
        if "mask" in line:
            bitMask = line[7:]
        else:
            # these two lines do a regex search for everything inside square brackets
            strAdress = re.search("\[(.*?)\]", line).group(0)
            # and then cast the result of that search to an int (removing the square brackets)
            memAdress = int(strAdress[1:len(strAdress) - 1]) 

            # search for everything after "= " and then cast it to a binary number as a string (Cuts of "0b" at the start)
            preMaskBits = bin(int(re.search("\= (.*)", line).group(0)[2:]))[2:]

            #self-explanatory
            setValuesBitByBit(bitMask, preMaskBits)
            cache[memAdress] = int(setValuesBitByBit(bitMask, preMaskBits), base=2)
            print(cache[memAdress])


run(data, cache)
res = 0
for item in cache:
    res += item

print(res)