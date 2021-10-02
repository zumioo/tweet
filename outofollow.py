""" 
使うときはコメントアウト外してね
import tweepy
import calendar
import random
import time
 
def main():
    consumer_key = 'XXXXX'
    consumer_secret = 'XXXXX'
    access_token_key = 'XXXXX'
    access_token_secret = 'XXXXX'
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    #keywordの内容を呟いたユーザーを自動フォロー
    keyword = ["おじいさん"]
    results = api.search(q=keyword,count=10)

    #サーチに引っかかったアカウントをフォローしてくよ
    for result in results:
        screen_name = result.user.screen_name　#ユーザーネームを取得
        print('@' + screen_name + 'をフォロー処理中です。')
        for i in range(3):
            #エラーに引っかかっても3回まではtryさせてあげるよ
            try:
                api.create_friendship(screen_name)
                print(screen_name + 'をフォローできました。')
            except tweepy.RateLimitError as e:
                #RateLimitErrorにかかったら15分待機するよ
                print(e)
                time.sleep(15 * 60)
            except tweepy.TweepError as e:
                #それ以外のエラーは処理を抜けて次の人に行くよ
                print(e)
                break
            else:
                #フォローがちゃんとできていたらTwitterを5秒休ませて次の人に行くよ
                time.sleep(5)
                break

main() 
"""