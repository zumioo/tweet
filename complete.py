""" from logging import log
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
    #各種変数を定義
    my_user_id = api.me().id_str #自分のidを取得
    follower_list = list(api.followers_ids(my_user_id))#自分のフォロワーを取得
    friend_list = list(api.friends_ids(my_user_id))#自分がフォローしている人を取得

    #各種関数を実行
    tweet(api)
    follow(api)
    follow_back(api,follower_list,friend_list)
    remove(api,follower_list,friend_list)

#0〜3000年の間でランダムな日付をツイート
def tweet(api):   
    year = random.randint(0,3000) #0~3000のランダムな数字を格納
    month = random.randint(1,12)  #1~12のランダムな数字を格納
    day31 = [1,3,5,7,8,10,12]     #31日まである月をリストにして格納
    day30 = [4,6,9,11]            #30日まである月をリストにして格納

    if (month in day31): 
        #もし31日まである月だったら
        day = random.randint(1,31)
    elif (month in day30): 
        #もし30日まである月だったら
        day = random.randint(1,30)        
    elif month == 2: 
        #2月の場合は閏年も考慮する
        if calendar.isleap(year):
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)            

    #取得した年月日をツイート
    api.update_status('今は' + str(year) + '年' + str(month) + '月' + str(day) + '日です。')

#keywordの内容を呟いたユーザーを自動フォロー
def follow(api):
    keyword = ["おじいさん"]
    results = api.search(q=keyword,count=10)

    for result in results:
        screen_name = result.user.screen_name
        print('@' + screen_name + 'をフォロー処理中です。')
        for i in range(3):
            try:
                api.create_friendship(screen_name)
                print(screen_name + 'をフォローできました。')
            except tweepy.RateLimitError as e:
                print(e)
                time.sleep(15 * 60)
            except tweepy.TweepError as e:
                print(e)
                break
            else:
                time.sleep(5)
                break

#フォロワーを自動でフォローバックする
def follow_back(api,follower_list,friend_list):   
    des_word = ['お金','FX','株','簡単に稼げる'] #自己紹介文に入っていたら嫌なワードをリスト化
    result = list(set(follower_list) - set(friend_list))#差分を計算

    if not result == [] :#resultがリストかつ空の要素であるか確認する
        for follower in result:
            print('@' + api.get_user(follower).screen_name + 'をフォロー処理中です。')
            data = api.get_user(follower).description
            if (False not in[i in data for i in des_word]):#リスト内包表記を使い慎重にフォローする
                print(api.get_user(follower).screen_name + 'はフォローしませんでした。')
                pass
            else:
                api.create_friendship(follower)
                print(api.get_user(follower).screen_name + 'をフォローできました。')
    else :
        print("おじいさんがフォローバックしていないフォロワーがいません。")

#フォロバしてくれない人のフォローを外す
def remove(api,follower_list,friend_list):
    result = list(set(friend_list) - set(follower_list))#差分を計算

    if not result == []:
        for un_follower in result:
            api.destroy_friendship(un_follower)
            print(api.get_user(un_follower).screen_name + 'のフォローを外しました。')
    else:
        print("おじいさんをフォローバックしていないフォロワーはいません。")




main()

 """