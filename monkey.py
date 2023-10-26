import random

def generateOne(strlen, beststr, status):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(strlen):
        if status[i] == False:
            result = result + alphabet[random.randrange(27)]
        else:
            result = result + beststr[i]
    return result

def score(goalstr, teststr, status):
    numright = 0
    for i in range(len(goalstr)):
        if goalstr[i] == teststr[i]:
            status[i] = True
            numright = numright +1
    return numright / len(goalstr)

def main():
    goalstr = "methinks it is like a weasel"
    bestscore = 0
    beststr = ""
    status = [False] * len(goalstr)
    newstr = generateOne(len(goalstr), beststr, status)
    newscore = score(goalstr, newstr, status)
    i = 1
    while  newscore < 1:
        if newscore > bestscore:
            print ("Update best - found: ", status.count(True), " new: ", newscore, " old: ", bestscore, " new: ", newstr, " old: ", beststr, " interation :", i)
            bestscore = newscore
            beststr = newstr
        if i % 1000 == 0:
            print ("working: ", bestscore, beststr, " interation :", i)
        i = i + 1
        newstr = generateOne(len(goalstr), beststr, status)
        newscore = score(goalstr, newstr, status)      
    if newscore > bestscore:
        bestscore = newscore
        beststr = newstr      
    print ("Complete: ", bestscore, beststr, " interation :", i)

main()