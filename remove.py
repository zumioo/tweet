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

    my_user_id = api.me().id_str #自分のidを取得
    follower_list = list(api.followers_ids(my_user_id))#自分のフォロワーを取得
    friend_list = list(api.friends_ids(my_user_id))#自分がフォローしている人を取得
    remove(api,follower_list,friend_list)
    
#フォロバしてくれない人のフォローを外す
def remove(api,follower_list,friend_list):
    result = list(set(friend_list) - set(follower_list))#差分を計算

    if not result == []:
        for un_follower in result:
            api.destroy_friendship(un_follower)
            print(api.get_user(un_follower).screen_name + 'のフォローを外しました。')
    else:
        print("おじいさんをフォローバックしていないフォロワーはいません。")

main() """

