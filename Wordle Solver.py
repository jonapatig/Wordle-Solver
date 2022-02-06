import tkinter as tk
import os

print(os.getcwd())

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
        good2 = [better[-1], better[-2], better[-3], better[-4], better[-5], better[-6], better[-7], better[-8], better[-9], better[-10]]
    else:
        if not better:
            good2 = ['No more words without duplicate letters']
        else:
            good2 = better
    return good2
def findgood3():
    global possible
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
    if len(possible2) > 10:
        good3 = [possible2[-1], possible2[-2], possible2[-3], possible2[-4], possible2[-5], possible2[-6], possible2[-7], possible2[-8], possible2[-9], possible2[-10]]
    else:
        good3 = reversed(possible2)
    return good3
def bubblesortpossible():
    global yellows
    sortedweights = []
    for i in possible:
        weight = 0
        if not i[0] in yellows:
            weight += counts0[i[0]]
        if not i[1] in yellows:
            weight += counts1[i[1]]
        if not i[2] in yellows:
            weight += counts2[i[2]]
        if not i[3] in yellows:
            weight += counts3[i[3]]
        if not i[4] in yellows:
            weight += counts4[i[4]]
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
    global possible, c1, c2, c3, c4, c5, input, yellows
    yellows = []
    grey = ""
    greys = []
    yellow1, yellow2, yellow3, yellow4, yellow5 = "", "", "", "", ""
    green1, green2, green3, green4, green5 = "", "", "", "", ""

    #Declare all grey letters
    if c1 == 0:
        grey += input[0]
    if c2 == 0:
        grey += input[1]
    if c3 == 0:
        grey += input[2]
    if c4 == 0:
        grey += input[3]
    if c5 == 0:
        grey += input[4]

    #Declare all yellow letters
    if c1 == 1:
        yellows.append(input[0])
        yellow1 = input[0]
    if c2 == 1:
        yellows.append(input[1])
        yellow2 = input[1]
    if c3 == 1:
        yellows.append(input[2])
        yellow3 = input[2]
    if c4 == 1:
        yellows.append(input[3])
        yellow4 = input[3]
    if c5 == 1:
        yellows.append(input[4])
        yellow5 = input[4]

    #Declare all green letters
    if c1 == 2:
        yellows.append(input[0])
        green1 = input[0]
    if c2 == 2:
        yellows.append(input[1])
        green2 = input[1]
    if c3 == 2:
        yellows.append(input[2])
        green3 = input[2]
    if c4 == 2:
        yellows.append(input[3])
        green4 = input[3]
    if c5 == 2:
        yellows.append(input[4])
        green5 = input[4]

    #Delete stuff from possible according to colors
    if yellows:
        deleters = []
        for letter in yellows:
            for i in possible:
                if not letter in i:
                    deleters.append(i)
        deleters = list(dict.fromkeys(deleters))
        for i in deleters:
            possible.remove(i)
    if grey:
        for i in grey:
            greys.append(i)
    if greys:
        deleters = []
        for letter in greys:
            for i in possible:
                if letter in i:
                    if not i.count(letter) > greys.count(letter): #If a letter appears twice in a guess, but only once in the word, program will no longer delete all options
                        deleters.append(i)
        deleters = list(dict.fromkeys(deleters))
        for i in deleters:
            possible.remove(i)
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
#_______________________________________________________________________________
#SET UP GUI STUFF
#_______________________________________________________________________________
def changecolor1():
    global c1, ting1, button1
    c1 += 1
    if c1 == 3:
        c1 = 0
    button1['text'] = ting1
    button1['bg'] = colors[c1]
    button1['activebackground'] = colors[c1]
def changecolor2():
    global c2, ting2, button2
    c2 += 1
    if c2 == 3:
        c2 = 0
    button2['text'] = ting2
    button2['bg'] = colors[c2]
    button2['activebackground'] = colors[c2]
def changecolor3():
    global c3, ting3, button3
    c3 += 1
    if c3 == 3:
        c3 = 0
    button3['text'] = ting3
    button3['bg'] = colors[c3]
    button3['activebackground'] = colors[c3]
def changecolor4():
    global c4, ting4, button4
    c4 += 1
    if c4 == 3:
        c4 = 0
    button4['text'] = ting4
    button4['bg'] = colors[c4]
    button4['activebackground'] = colors[c4]
def changecolor5():
    global c5, ting5, button5
    c5 += 1
    if c5 == 3:
        c5 = 0
    button5['text'] = ting5
    button5['bg'] = colors[c5]
    button5['activebackground'] = colors[c5]
def submit():
    global window, suggestedwindow
    window.destroy()
    suggestedwindow()
def submit2():
    global input, window2
    rawinput = wordinput.get()
    if not rawinput or len(rawinput) < 5:
        input = "lover"
    else:
        input = rawinput[0:5]
    window2.destroy()
    wordcolors()
def submit3():
    global window3, selectword
    window3.destroy()
    selectword()
def selectword():
    global wordinput, window2, startlen, possible, starting
    window2 = tk.Tk()
    startlen = len(possible)
    if starting == 1:
        window2.geometry('800x150+560+400')
    else:
        window2.geometry('400x150+760+400')
    window2.title('Suggested Guess')
    wordinput = tk.Entry(window2, width=10, bg="white")
    submitbutton2 = tk.Button(window2, text = "Submit", command=submit2)
    submitbutton2.place(relx=0.5,rely=0.8,anchor="center")
    if starting == 1:
        wordinput.place(relx=0.5,rely=0.55,anchor="center")
    else:
        wordinput.place(relx=0.5,rely=0.4,anchor="center")
    if starting == 1:
        starting = 0
        gd2 = findgood2()
        gd3 = findgood3()
        gdstart = "Good starters excluding duplicate letters: "
        for i in gd2:
            gdstart += i + ", "
        gdstart = gdstart[:-2]
        gdstart+="."
        gdstart += "\n\nStarters optimized for vowels: "
        for i in gd3:
            gdstart += i + ", "
        gdstart = gdstart[:-2]
        gdstart+="."
        goodstarters = tk.Label(window2, text = gdstart)
        goodstarters.place(relx=0.5,rely=0.25,anchor="center")
    window2.attributes('-topmost', True)
    window2.mainloop()
def wordcolors():
    global ting1, ting2, ting3, ting4, ting5, button1, button2, button3, button4, button5, colors, input, c1, c2, c3, c4, c5, window
    window = tk.Tk()
    window.geometry('400x150+760+400')
    window.title('Worlde Output')
    c1,c2,c3,c4,c5 = 0,0,0,0,0
    colors = ["grey", "yellow", "green2"]
    ting1 = input[0]
    ting2 = input[1]
    ting3 = input[2]
    ting4 = input[3]
    ting5 = input[4]
    button1 = tk.Button(window, text = ting1, bg=colors[c1], command=changecolor1, activebackground = colors[c1])
    button2 = tk.Button(window, text = ting2, bg=colors[c2], command=changecolor2, activebackground = colors[c2])
    button3 = tk.Button(window, text = ting3, bg=colors[c3], command=changecolor3, activebackground = colors[c3])
    button4 = tk.Button(window, text = ting4, bg=colors[c4], command=changecolor4, activebackground = colors[c4])
    button5 = tk.Button(window, text = ting5, bg=colors[c5], command=changecolor5, activebackground = colors[c5])
    submitbutton = tk.Button(window, text = "Submit", command = submit)
    button1.place(relx=.40, rely=.5, anchor="center")
    button2.place(relx=.45, rely=.5, anchor="center")
    button3.place(relx=.50, rely=.5, anchor="center")
    button4.place(relx=.55, rely=.5, anchor="center")
    button5.place(relx=.60, rely=.5, anchor="center")
    submitbutton.place(relx=.5, rely=0.9, anchor="center")
    window.attributes('-topmost', True)
    window.mainloop()
def suggestedwindow():
    global findgood, findgood2, findgood3, main, submit3, window3, bubblesortpossible, startlen, possible
    main()
    if not startlen == len(possible):
        bubblesortpossible()
    startlen = len(possible)
    window3 = tk.Tk()
    window3.geometry('800x150+560+400')
    window3.title('Suggested Attempts')
    if len(possible) > 0:
        gd1 = findgood()
        gd2 = findgood2()
        gd = "Try (including duplicate letters included): "
        for i in gd1:
            gd += i + ", "
        gd = gd[:-2]
        gd+="."
        gd += "\n\nTry (excluding duplicate letters): "
        for i in gd2:
            gd += i + ", "
        gd = gd[:-2]
        gd+="."
        gd+="\n\nChance of success: "+str((1/len(possible))*100)+"%"
    else:
        gd="\n\n\n\nYou input something wrong. You're dumb."
    goodtext = tk.Label(window3, text = gd)
    submitbutton3 = tk.Button(window3, text = "Continue", command = submit3)
    exitbutton = tk.Button(window3, text = "Done", command = quit)
    restartbutton = tk.Button(window3, text = "Restart", command = restart)
    goodtext.pack()
    submitbutton3.place(relx = .5, rely = 0.9, anchor = "center")
    exitbutton.place(relx = .4, rely = 0.9, anchor = "center")
    restartbutton.place(relx = .6, rely = 0.9, anchor = "center")
    window3.attributes('-topmost', True)
    window3.mainloop()
def quit():
    global window3
    window3.destroy()
    exit()
def restart():
    global raw, window3, possible, startlen, starting
    with open('5letterwords.txt', 'r') as f:
        raw = f.read()
    possible = raw.splitlines()
    window3.destroy()
    starting = 1
    selectword()
#_______________________________________________________________________________
# CODE ON RUN:
#_______________________________________________________________________________
starting = 1
selectword()
