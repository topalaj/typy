from getkey import getkey, keys
from termcolor import colored
import sys
import os
import time
import random

# for printing via sys.stdout
def sysprint(inputstring):
    sys.stdout.write(inputstring)
    sys.stdout.flush()

# just a countdown
def countdown():
    os.system('clear')
    print("3")
    time.sleep(1)
    os.system('clear')
    print("2")
    time.sleep(1)
    os.system('clear')
    print("1")
    time.sleep(1)
    os.system('clear')

# print the screen including the information
def printScreen(error):
    os.system('clear')
    timer = time.time() - start
    wpm = ((overallWordCount)/timer)*60
    print("WPM: {:.0f}      Words: {}/{}       Time: {:.5}s     Sentences: {}/{}".format(wpm, i, wordCount, timer, done, challengeCount))
    print("")
    for j in range(wordCount):
        if ( j < i ):
            sysprint(colored(words[j], 'green')+" ")
        elif ( j == i and error == 1 ):
            sysprint(colored(words[j], 'red')+" ")
        else:
            sysprint(words[j]+" ")
    print("\n")

# characters which can be used
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'?!:;-_"

# open a file and save it line by line in challenge
f = open("sentences","r")
challenge = f.readlines()

# initializing
overallWordCount = 0
done = 0
wpm = 0

# welcome screen
os.system('clear')
print("How much sentences do you want to type?")
challengeCount = int(input())
countdown()

# timer start
start = time.time()

while(done < challengeCount):
    i=0
    string=""
    randomChallenge = random.choice(challenge)
    words = randomChallenge.split()
    wordCount = len(words)
    printScreen(0)
    while (i != wordCount):
        key = getkey()
        if (key == " " or key == keys.ENTER ):
            if(string == words[i]):
                i+=1
                overallWordCount+=1
                printScreen(0)
                string = ""
                continue
            else:
                printScreen(1)
                string = ""
                continue
        if (key == keys.BACKSPACE):
            sysprint("\b \b")
            string = string[:-1]
            continue
        sysprint(key)
        for letter in alphabet:
            if key == letter:
                string = string + letter
    done+=1

# end screen
printScreen(0)
duration = time.time() - start
print("You took {:.5}s for {} words.".format(duration,overallWordCount))
