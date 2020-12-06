with open("day6input.md") as source:
    data = source.read()
data = data.split("\n\n")
data = [item.split("\n") for item in data]


def findCountOfDistinctAnswers(data):
    sumAnswers = 0
    for group in data:
        distinctAnswers = []
        for person in group:
            for answer in person:
                if answer not in distinctAnswers:
                    distinctAnswers.append(answer)
        sumAnswers += len(distinctAnswers)
    return sumAnswers


def findQuestionsWithAllMatches(data):
    sumAnswers = 0
    for group in data:
        groupAnswers = []
        for person in group:
            for answer in person:
                groupAnswers.append(answer)
        matches = []
        for item in groupAnswers:
            if groupAnswers.count(item) == len(group) and item not in matches:
                matches.append(item)
        sumAnswers += len(matches)
    return sumAnswers

print(findCountOfDistinctAnswers(data))
print("part two: ", findQuestionsWithAllMatches(data))
                