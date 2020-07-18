import tweepy
import config
import time
import requests
import linecache
import json
import random
#---------------------------------------------------------
CK = config.CK
CS = config.CS
AT = config.AT
ATS = config.ATS
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)
#---------------------------------------------------------

dick = {}



while True:
    print("**************************************")
    print("ツイートまで")
    time.sleep(1)
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    times = [32, 54, 354, 876, 345, 123, 999, 257, 334, 98, 10, 1, 100, 1293, 910, 1278, 2918, 1957, 1374, 583, 70, 60, 37]
    times_1 = random.choice(times)
    for status in api.home_timeline(count=1, include_rts=False):
        text1 = status.text
        id = status.id
        ACNH = ["だなも", "だなも...", "だなも！！", "ぴえん", "🥺", "ふんふん", "₍₍(ง •ᴗ•)ว ⁾⁾ ₍₍(ง •ᴗ•)ว ⁾⁾", ""]
        TweetTxt = (text1 + random.choice(ACNH))
        dick.update({id:TweetTxt})
        if '@' in dick[id]:
            print("画像やurl、メンションが含まれていたのでスキップします。")
            time.sleep(60)
        else:
            if(status.entities["urls"]!=[] or ("media"or"is_quote_status") in status.entities):
                print("画像やurl、メンションが含まれていたのでスキップします。")
                time.sleep(60)
            else:
                print('-------------------------------------------')
                print(TweetTxt)
                try:
                    api.update_status(TweetTxt)
                    api.create_favorite(id)
                    print("Succeeded!")
                    print("次のツイートまで" + str(times_1+10) + "秒")
                    time.sleep(times_1)
                except:
                    print("Succeeded!")
                    print("次のツイートまで" + str(times_1+10) + "秒")
                    time.sleep(times_1)
