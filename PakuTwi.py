import tweepy
import config
import time
import requests
import linecache
import json
#---------------------------------------------------------
CK = config.CK
CS = config.CS
AT = config.AT
ATS = config.ATS
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)
#---------------------------------------------------------
while True:
    for status in api.home_timeline(count=1):
        text1 = status.text
        print('-------------------------------------------')
        print('name:' + status.user.name)
        print(text1)
        api.update_status(text1)
        print("Succeeded!")
        time.sleep(60)