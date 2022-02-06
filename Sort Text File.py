with open('5letterwords.txt', 'r') as f:
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

bubblesortpossible()
if possible[0] != "yukky":
    with open('5letterwords.txt', 'w') as e:
        for i in possible:
            e.write(i)
            e.write("\n")

with open('5lettervowels.txt', 'r') as f:
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
    with open('5lettervowels.txt', 'w') as e:
        for i in possible2:
            e.write(i)
            e.write("\n")
