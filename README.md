# Wordle-Solver
This is a program I made for fun after finding out about the viral word game wordle. Using bubble sorting, it will always give the user the guess which will
eliminate the most words from the remaining list.

# How to use it
As long as both text files are present in the same folder as the wordle solver.py file, and python3 and tkinter are installed, the program will run. 

More words can be added to the 5letterwords text file. Running the sorting script will bubble sort the file and add to the vowel file before the program is run,
in order to make the startup time nearly instant. As of now, only possible solutions (taken directly from the wordle source code) are listed in the 5letterwords
file.

When running the wordle solver, the first window requires an input of the current attempt. Clicking submit will take you to the next window, which allows you to 
cycle through the color of each letter by clicking on it. Pressing submit here will remove all words that it can't be, and sort the remaining words by the amount
of words that the remaining unknown letters will eliminate. Pressing done on the next window will exit the program, while the continue button will continue the
current attempt. Restart will reset all possible words and give the "good starting words" on the first window again.
