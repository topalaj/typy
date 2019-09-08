from getkey import getkey, keys
import sys

string = ""

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'"

challenge = "Ich bin Toni Hansen."

words = challenge.split()

print(words)

print(challenge)

i = 0

wordCount = len(words)

while 1:
    key = getkey()
    if key == " ":
        if(string == words[i]):
            if(i+1 == wordCount):
                print("\nGewonnen!")
                exit()
            sys.stdout.write(" ")
            sys.stdout.flush()
            i+=1
            string = ""
            continue
        else:
            continue
    if key == keys.BACKSPACE:
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        string = string[:-1]
        continue
    sys.stdout.write(key)
    sys.stdout.flush()
    for letter in alphabet:
        if key == letter:
            string = string + letter
