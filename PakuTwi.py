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
    #ツイートまでのカウントダウン
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
    #ランダムで待機時間を選択
    times = [32, 54, 354, 876, 345, 123, 999, 257, 334, 98, 10, 1, 100, 1293, 910, 1278, 2918, 1957, 1374, 583, 70, 60, 37]
    times_1 = random.choice(times)
    for status in api.home_timeline(count=1, include_rts=False): #Twitterのタイムラインから1つ取得+RTを除く
        text1 = status.text #ツイート内容をtext1に代入
        id = status.id #ツイートIDをidに代入
        dick.update({id:text1})
        if '@' in dick[id]:#ツイート内容にメンションが含まれてるかの判別
            print("画像やurl、メンションが含まれていたのでスキップします。")
            time.sleep(60)
        else: #含まれていなかった場合↓の内容を実行
            if(status.entities["urls"]!=[] or ("media"or"is_quote_status") in status.entities):#URLや画像が含まれているかの判定
                print("画像やurl、メンションが含まれていたのでスキップします。")
                time.sleep(60)
            else:#含まれて居なかった場合↓の内容を実行
                print('-------------------------------------------')
                print('name:' + status.user.name)#コマンドプロンプトにユーザー名を表示
                print(text1)#タイムラインにツイート内容を表示
                try:
                    api.update_status(text1)#text1に代入してるツイート内容を自分のアカウトでツイート
                    api.create_favorite(id)#そのツイートをいいね
                    print("Succeeded!")
                    print("次のツイートまで" + str(times_1+10) + "秒")#次のツイートまでの時間をコマンドプロンプトに表示
                    time.sleep(times_1)
                except:#もし上の内容でエラーが発生した場合↓の内容を実行(ツイートとかいいねでAPI制限が起きることがあるので)
                    print("Error!")
                    print("次のツイートまで" + str(times_1+10) + "秒")
                    time.sleep(times_1)
