from getkey import getkey, keys
from termcolor import colored
import sys
import os
import time
import random

def sysprint(inputstring):
    sys.stdout.write(inputstring)
    sys.stdout.flush()

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

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'?!:;-_"

#challenge = ["Lore ipsum dolor sit amet.", "Bananen sind gesund.", "Ich bin Toni Hansen."]
f = open("sentences","r")
challenge = f.readlines()
overallWordCount = 0
done = 0
wpm = 0

os.system('clear')
print("How much sentences do you want to type?")
challengeCount = int(input())
countdown()

start = time.time()

while(done < challengeCount):
    i=0
    j=0
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
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            string = string[:-1]
            continue
        sys.stdout.write(key)
        sys.stdout.flush()
        for letter in alphabet:
            if key == letter:
                string = string + letter
    done+=1

printScreen(0)
duration = time.time() - start
print("You took {:.5}s for {} words.".format(duration,overallWordCount))
