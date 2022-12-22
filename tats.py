import time
from datetime import datetime
from random import randrange
from time import sleep
from json import load
from mastodon import Mastodon
from twython import Twython

print('Starting Hand Tats service at ' + str(datetime.now()))

with open('secrets.json') as secretsfile:
    secrets = load(secretsfile)

with open('wordlist.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

def generate_tat():
    firstWord = words[randrange(len(words))]
    secondWord = words[randrange(len(words))]

    return '👊' + firstWord.upper() + ' ' + secondWord.upper() + '👊'

def tweet(tat):
    try:
        twitter = Twython(
            secrets['TWITTER_APP_KEY'],
            secrets['TWITTER_APP_SECRET'],
            secrets['TWITTER_USER_TOKEN'],
            secrets['TWITTER_USER_SECRET'])

        twitter.update_status(status=tat)
        print('Tweeted at' + str(datetime.now()) + ': ' + tat)
    except Exception as e:
        print(e)

def toot(tat):
    try:
        mastodon = Mastodon(access_token=secrets['MASTODON_ACCESS_TOKEN'], api_base_url="https://botsin.space")
        mastodon.toot(tat)
        print('Tooted at' + str(datetime.now()) + ': ' + tat)
    except Exception as e:
        print(e)

def post_all():
    tat = generate_tat()
    tweet(tat)
    toot(tat)

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

post_all()
do_every(4 * 60 * 60, post_all)
