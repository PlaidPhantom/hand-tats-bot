from random import randrange


with open('4letters.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

for x in range(0, 10):
    firstWord = words[randrange(len(words))]
    secondWord = words[randrange(len(words))]

    print(str(x) + ': ', firstWord, secondWord)
