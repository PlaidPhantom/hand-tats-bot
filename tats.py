from random import randrange
from time import sleep


with open('wordlist.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

while True:
    firstWord = words[randrange(len(words))]
    secondWord = words[randrange(len(words))]

    print(firstWord, secondWord)

    sleep(5)
