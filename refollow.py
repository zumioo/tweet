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

    #フォロワーを自動でフォローバックする
    my_user_id = api.me().id_str #自分のidを取得
    des_word = ['お金','FX','株','簡単に稼げる'] #自己紹介文に入っていたら嫌なワードをリスト化
    follower_list = [] 
    friend_list = []

    follower_list = api.followers_ids(my_user_id)#自分のフォロワーを取得
    friend_list = api.friends_ids(my_user_id)#自分がフォローしている人を取得

    result = list(set(follower_list) - set(friend_list))#差分を計算

    if not result == [] :#resultがリストかつ空の要素であるか確認する
        for follower in result:
            data = api.get_user(follower).description #フォローする人の紹介文を取得
            if (False not in[i in data for i in des_word]):#リスト内包表記を使い慎重にフォローする
                pass
            else:
                api.create_friendship(follower)
    else :
        print("フォローバックしていないフォロワーがいません。")

main() """

