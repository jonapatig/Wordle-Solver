try:
    with open('C:/Users/Jona/github/Wordle-Solver/5letterwords.txt', 'r') as f:
        raw = f.read()
except:
    with open('C:/Users/jonap/github/Wordle-Solver/5letterwords.txt', 'r') as f:
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
    for i in possible:
        stop = 0
        for l in i:
            if i.count(l) > 1:
                stop = 1
        if stop == 0:
            better.append(i)
    if len(better) >= 10:
        # good2 = [better[0], better[1], better[2], better[3], better[4], better[5], better[6], better[7], better[8], better[9]]
        good2 = [better[-1], better[-2], better[-3], better[-4], better[-5], better[-6], better[-7], better[-8], better[-9], better[-10]]
    else:
        if not better:
            good2 = ['No more words without duplicate letters']
        else:
            good2 = better
    return good2

def findgood3():
    global possible
    try:
        with open('C:/Users/jonap/github/Wordle-Solver/5lettervowels.txt', 'r') as f:
            vowelraw = f.read()
    except:
        with open('C:/Users/Jona/github/Wordle-Solver/5lettervowels.txt', 'r') as f:
            vowelraw = f.read()
    possible2 = vowelraw.splitlines()
    if not possible2:
        possible2 = possible
        vowelpoints = []
        for i in possible2:
            points = 0
            vowellist = ['a','e','i','o','u']
            for a in i:
                if a in vowellist:
                    points += 1
                    vowellist.remove(a)
            vowelpoints.append(points)
        for x in range(0,len(vowelpoints)):
            for i in range(0,(len(vowelpoints)-x)):
                if not i == (len(vowelpoints)-1) and vowelpoints[i] > vowelpoints[i+1]:
                    temp = vowelpoints[i+1]
                    temp2 = possible2[i+1]
                    vowelpoints[i+1] = vowelpoints[i]
                    possible2[i+1] = possible2[i]
                    vowelpoints[i] = temp
                    possible2[i] = temp2
    if len(possible2) > 10:
        good3 = [possible2[-1], possible2[-2], possible2[-3], possible2[-4], possible2[-5], possible2[-6], possible2[-7], possible2[-8], possible2[-9], possible2[-10]]
    else:
        good3 = reversed(possible2)
    return good3

def bubblesortpossible():
    sortedweights = []
    for i in possible:
        weight = counts0[i[0]] + counts1[i[1]] + counts2[i[2]] + counts3[i[3]] + counts4[i[4]]
        sortedweights.append(weight)
    for x in range(0,len(sortedweights)):
        for i in range(0,(len(sortedweights)-x)):
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

    yellow = input("\nInput yellow and green letters (press enter if there are none): ")
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

    grey = input("\nInput grey letters (press enter if there are none): ")
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
    yellow1 = input("\nInput yellow letter in position 1 (press enter if position 1 isn't yellow): ")
    yellow2 = input("\nInput yellow letter in position 2 (press enter if position 2 isn't yellow): ")
    yellow3 = input("\nInput yellow letter in position 3 (press enter if position 3 isn't yellow): ")
    yellow4 = input("\nInput yellow letter in position 4 (press enter if position 4 isn't yellow): ")
    yellow5 = input("\nInput yellow letter in position 5 (press enter if position 5 isn't yellow): ")

    if yellow1:
        deleters = []
        for i in possible:
            if i[0] == yellow1:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if yellow2:
        deleters = []
        for i in possible:
            if i[1] == yellow2:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if yellow3:
        deleters = []
        for i in possible:
            if i[2] == yellow3:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if yellow4:
        deleters = []
        for i in possible:
            if i[3] == yellow4:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)
    if yellow5:
        deleters = []
        for i in possible:
            if i[4] == yellow5:
                deleters.append(i)
        if deleters:
            for i in deleters:
                possible.remove(i)

    green1 = input("\nInput green letter in position 1 (press enter if position 1 isn't green): ")
    green2 = input("\nInput green letter in position 2 (press enter if position 2 isn't green): ")
    green3 = input("\nInput green letter in position 3 (press enter if position 3 isn't green): ")
    green4 = input("\nInput green letter in position 4 (press enter if position 4 isn't green): ")
    green5 = input("\nInput green letter in position 5 (press enter if position 5 isn't green): ")

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
    print('\nIncluding double letter words: ', findgood())
    print('\nNo duplicate letter words: ', findgood2())


#_______________________________________________________________________________
# CODE ON RUN:
#_______________________________________________________________________________
startlen = len(possible)
while True:
    solved = 'no'
    if possible[0] != "yukky":
        bubblesortpossible()
    print('\nGood starters to find green letters: ', findgood())
    print('\nGood starters excluding any duplicate letters: ', findgood2())
    print('\nGood starter optimized for vowels: ', findgood3())
    while True:
        main()
        if len(possible) != startlen:
            bubblesortpossible()
        print('\nChance of success: ', (1/len(possible))*100,'%')
        print("Solved? (Type 'yes' to restart the program. Type 'exit' to quit the program)")
        solved = input()
        if solved == 'yes' or solved == 'exit':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break
    try:
        with open('C:/Users/jonap/github/Wordle-Solver/5letterwords.txt', 'r') as f:
            raw = f.read()
    except:
        with open('C:/Users/Jona/github/Wordle-Solver/5letterwords.txt', 'r') as f:
            raw = f.read()
    possible = raw.splitlines()
    if solved == 'exit':
        break
exit()

fuck you fried
