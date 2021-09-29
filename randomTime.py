""" 使うときはコメントアウト外してね
import tweepy
import calendar
import random
 
def main():
    consumer_key = 'XXXXX'
    consumer_secret = 'XXXXX'
    access_token_key = 'XXXXX'
    access_token_secret = 'XXXXX'
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    #0〜3000年の間でランダムな日付をツイート
    year = random.randint(0,3000)
    month = random.randint(1,12)
    day31 = [1,3,5,7,8,10,12]
    day30 = [4,6,9,11]

    if (month in day31):
        day = random.randint(1,31)
    elif (month in day30):
        day = random.randint(1,30)        
    elif month == 2:
        if calendar.isleap(year):
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)            

    api.update_status('今は' + str(year) + '年' + str(month) + '月' + str(day) + '日です。')

main() """
