#!/usr/bin/python
#     __
#    / /___ __  ___  __ __
#   / __/ // / / _ \/ // /
#   \__/\_, (_) .__/\_, /
#      /___/ /_/   /___/


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
def printScreen():
    os.system('clear')
    timer = time.time() - start
    wpm = ((overallWordCount)/timer)*60
    print("WPM: {:.0f}      Words: {}/{}       Time: {:.3}s     Sentences: {}/{}    Mistakes: {}".format(wpm, i, wordCount, timer, done, challengeCount, mistakes))
    print("")
    for j in range(wordCount):
        if ( j < i ):
            sysprint(colored(words[j], 'green')+" ")
        elif ( j == i ):
            for index in range(min(len(string),len(words[i]))):
                if ( words[i][index] == string[index] ):
                   sysprint( colored(words[i][index],'green'))
                elif ( words[i][index] != string[index] ):
                    sysprint( colored(words[i][index],'red'))
            for restIndex in range(min(len(string),len(words[i])), len(words[i])):
                sysprint( words[i][restIndex] )
            sysprint(" ")
        else:
            sysprint(words[j]+" ")
    print("\n")
    sysprint(string)

# characters which can be used
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'?!:;-_"

# open a file and save it line by line in challenge
f = open("sentences","r")
challenge = f.readlines()

# initializing
overallWordCount = 0
done = 0
wpm = 0
mistakes = 0

# welcome screen
os.system('clear')
print("{} sentences loaded.".format(len(challenge)))
challengeCount=0
print("How many sentences do you want to type?")
while(challengeCount<1 or challengeCount>len(challenge)):
  challengeCount = int(input())
  if (challengeCount<1 or challengeCount>len(challenge)):
    os.system('clear')
    print("Please enter an amount between 0 and {}:".format(len(challenge)))
countdown()

# timer start
start = time.time()

while(done < challengeCount):
    i=0
    string=""
    randomChallenge = random.choice(challenge)
    challenge.remove(randomChallenge)
    words = randomChallenge.split()
    wordCount = len(words)
    while (i != wordCount):
        printScreen()
        key = getkey()
        if (key == " " or key == keys.ENTER ):
            if(string == words[i]):
                i+=1
                overallWordCount+=1
                printScreen()
                string = ""
                continue
            else:
                mistakes+=1
                printScreen()
                string = ""
                continue
        if (key == keys.BACKSPACE):
            string = string[:-1]
            continue
        for letter in alphabet:
            if key == letter:
                string = string + letter
    done+=1

# end screen
printScreen()
duration = time.time() - start
print("You took {:.5}s for {} words.".format(duration,overallWordCount))
