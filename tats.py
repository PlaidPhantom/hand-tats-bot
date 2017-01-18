from random import randrange
from time import sleep
from json import load

from twython import Twython

with open('secrets.json') as secretsfile:
    secrets = load(secretsfile)


with open('wordlist.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

twitter = Twython(secrets['APP_KEY'], secrets['APP_SECRET'], secrets['OAUTH_TOKEN'], secrets['OAUTH_TOKEN_SECRET'])

while True:
    firstWord = words[randrange(len(words))]
    secondWord = words[randrange(len(words))]

    tat = firstWord.upper() + ' ' + secondWord.upper()

    # print(tat)
    twitter.update_status(status=tat)

    sleep(5)
