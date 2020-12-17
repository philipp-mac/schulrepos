from time import perf_counter 

startingnums = (1,0,15,2,10,13)

def addOrUpdateDicts(number, mdict, tdict, i):
    if number in mdict.keys():
        mdict[number] = [mdict[number][len(mdict[number]) - 1], i]
        tdict[number] += 1
    else:
        mdict.update({number: [i]})
        tdict.update({number: 1})

def play(startingnums, limit):
    mentions = {}
    timesMentioned = {}
    lastNumber = 0
    timeStart = perf_counter()

    for i in range(len(startingnums)):
        mentions[startingnums[i]] = [i]
        timesMentioned[startingnums[i]] = 1
        lastNumber = startingnums[i]

    for turn in range(len(startingnums), limit):
        
        if turn % 1000000 == 0:
            print("~~~ Turn Nr. ", turn, "~~~")
            timeStop = perf_counter()
            print("time elapsed: approx. ", timeStop - timeStart)

        if timesMentioned[lastNumber] == 1:
            lastNumber = 0
            addOrUpdateDicts(lastNumber, mentions, timesMentioned, turn)

        else:
            previousMentions = mentions[lastNumber][-2:]
            spoken = previousMentions[1] - previousMentions[0]
            addOrUpdateDicts(spoken, mentions, timesMentioned, turn)
            lastNumber = spoken

    return lastNumber
    

print(play(startingnums, 30000000))