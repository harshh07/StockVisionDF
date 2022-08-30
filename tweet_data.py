import tweepy
import csv
import pandas as pd
import datetime

consumer_key = 'x'
consumer_secret = 'x'
access_token = 'x'
access_token_secret = 'x'

tick=input("Enter the stock name: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


df = pd.DataFrame({"Dates":[], 
                    "Text":[]})
tweets = []
var1=tick+" stocks"

for tweet in tweepy.Cursor(api.search,q=var1,count=100,
                           lang="en").items():
    print (tweet.created_at, tweet.text)


    df_temp = pd.DataFrame({"Dates":[tweet.created_at], 
                    "Text":[tweet.text]})

    df=df.append(df_temp, ignore_index = True)
print(df)

var2=tick+'.csv'
df.to_csv(var2)



