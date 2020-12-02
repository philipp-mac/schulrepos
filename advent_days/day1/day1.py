with open("day1input.md") as source:
    expenses = source.readlines()
expenses = [item.strip() for item in expenses] 
expenses = [int(item) for item in expenses]

for i, number in enumerate(expenses[:-1]):
    complementary = 2020 - number
    if complementary in expenses[i+1:]:
        print("Solution is: {}*{} = {}".format(number, complementary, number*complementary))
        break