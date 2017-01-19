from random import randrange
from time import sleep
from json import load

from twython import Twython

with open('secrets.json') as secretsfile:
    secrets = load(secretsfile)


with open('wordlist.txt') as allWords:
    words = allWords.readlines()

words = [word.strip('\n') for word in words]

twitter = Twython(app_key=secrets['API_KEY'], app_secret=secrets['API_SECRET'], oauth_token=secrets['USER_TOKEN'], oauth_token_secret=secrets['USER_SECRET'])

twitter.update_status(status="👊hey world👊")

#while True:
#    firstWord = words[randrange(len(words))]
#    secondWord = words[randrange(len(words))]
#
#    tat = firstWord.upper() + ' ' + secondWord.upper()
#
#    # print(tat)
#    twitter.update_status(status=tat)
#
#    sleep(5)
