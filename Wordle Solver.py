try:
    with open('C:/Users/Jona/Documents/5letterwords.txt', 'r') as f:
        raw = f.read()
except:
    with open('C:/Users/jonap/Documents/5letterwords.txt', 'r') as f:
        raw = f.read()

possible = raw.splitlines()

counts0 = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
counts1 = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
counts2 = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
counts3 = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
counts4 = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}

for i in possible:
    counts0[i[0]]=counts0[i[0]]+1
    counts1[i[1]]=counts0[i[1]]+1
    counts2[i[2]]=counts0[i[2]]+1
    counts3[i[3]]=counts0[i[3]]+1
    counts4[i[4]]=counts0[i[4]]+1

def findgood():
    global possible
    if len(possible) > 10:
        good = [possible[-1],possible[-2],possible[-3],possible[-4],possible[-5],possible[-6],possible[-7], possible[-8],possible[-9], possible[-10]]
    else:
        good = possible
    return good
def findgood2():
    better = []
    for i in reversed(possible):
        stop = 0
        for l in i:
            if i.count(l) > 1:
                stop = 1
        if stop == 0:
            better.append(i)
        if len(better) > 10:
            good2 = [better[0], better[1], better[2], better[3], better[4], better[5], better[6], better[7], better[8], better[9]]
        else:
            good2 = better
    return good2

def bubblesortpossible():
    sortedweights = []
    for i in possible:
        weight = counts0[i[0]] + counts1[i[1]] + counts2[i[2]] + counts3[i[3]] + counts4[i[4]]
        sortedweights.append(weight)
    for x in range(0,len(sortedweights)):
        for i in range(0,len(sortedweights)):
            if not i == (len(sortedweights)-1) and sortedweights[i] > sortedweights[i+1]:
                temp = sortedweights[i+1]
                temp2 = possible[i+1]
                sortedweights[i+1] = sortedweights[i]
                possible[i+1] = possible[i]
                sortedweights[i] = temp
                possible[i] = temp2


def main():
    global possible
    yellows = []

    yellow = input("Input yellow and green letters (press enter if there are none): ")
    if yellow:
        for i in yellow:
            yellows.append(i)
    if yellows:
        deleters = []
        for letter in yellows:
            for i in possible:
                if not letter in i:
                    deleters.append(i)
        deleters = list(dict.fromkeys(deleters))
        for i in deleters:
            possible.remove(i)

    grey = input("Input grey letters (press enter if there are none): ")
    greys = []

    if grey:
        for i in grey:
            greys.append(i)
    if greys:
        deleters = []
        for letter in greys:
            for i in possible:
                if letter in i:
                    deleters.append(i)
        deleters = list(dict.fromkeys(deleters))
        for i in deleters:
            possible.remove(i)

    green1 = input("Input green letter in position 1 (press enter if position 1 isn't green): ")
    green2 = input("Input green letter in position 2 (press enter if position 1 isn't green): ")
    green3 = input("Input green letter in position 3 (press enter if position 1 isn't green): ")
    green4 = input("Input green letter in position 4 (press enter if position 1 isn't green): ")
    green5 = input("Input green letter in position 5 (press enter if position 1 isn't green): ")

    if green1:
        deleters = []
        for i in possible:
            if not i[0] == green1:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if green2:
        deleters = []
        for i in possible:
            if not i[1] == green2:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if green3:
        deleters = []
        for i in possible:
            if not i[2] == green3:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if green4:
        deleters = []
        for i in possible:
            if not i[3] == green4:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if green5:
        deleters = []
        for i in possible:
            if not i[4] == green5:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    print('Including double letter words: ', findgood())
    print('No double letter words: ', findgood2())

    global solved

    print("Solved?")
    solved = input()


#_______________________________________________________________________________
# CODE ON RUN:
#_______________________________________________________________________________

solved = 'no'
bubblesortpossible()
print('Good starters including double letter words: ', findgood())
print('Good starters excluding double letter words: ', findgood2())
while True:
    main()
    if solved == 'yes':
        exit()
