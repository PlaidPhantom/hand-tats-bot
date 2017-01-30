import time

from datetime import datetime
from random import randrange
from time import sleep
from json import load

from twython import Twython

print('Starting Hand Tats service at ' + str(datetime.now()))

with open('secrets.json') as secretsfile:
    secrets = load(secretsfile)

with open('wordlist.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

twitter = Twython(secrets['APP_KEY'], secrets['APP_SECRET'], secrets['USER_TOKEN'], secrets['USER_SECRET'])

#twitter.update_status(status="👊hey world👊")

def tweet():
    firstWord = words[randrange(len(words))]
    secondWord = words[randrange(len(words))]

    tat = '👊' + firstWord.upper() + ' ' + secondWord.upper() + '👊'

    print('Tweeted at' + str(datetime.now()) + ': ' + tat)
    twitter.update_status(status=tat)

# http://stackoverflow.com/questions/8600161/executing-periodic-actions-in-python
def do_every(period,f,*args):
    def g_tick():
        t = time.time()
        count = 0
        while True:
            count += 1
            yield max(t + count*period - time.time(),0)
    g = g_tick()
    while True:
        time.sleep(next(g))
        f(*args)

tweet()
do_every(4 * 60 * 60, tweet)
