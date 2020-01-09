import random, os, sys
import tweepy

a = open("a.txt", "r").readlines()
consumer_secret = "AQWEMsoARuMeIXJ4KSmJhBqpQoncgV5rpvQnHRXzjeUYoW9tBW"
consumer_key = "YhfGo9ZT2RqGM6hvRi3eNa2Ho"
access_token = "928670621776711680-fpvzbv6gWvKn37gJ3WL1UQQVk6LJClV"
access_token_secret = "iNGKyJNy7D5FwxmWPIAZjXqJPyWPMeGefnfT8nBxcpAfG"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if a[2]=="0":
    texto = a[0][0]+" + "+a[1][0]+" = " +str(int(a[0][0])+int(a[1][0]))
elif a[2]=="1":
    texto = a[0][0]+" x "+a[1][0]+" = " +str(int(a[0][0])*int(a[1][0]))
elif a[2]=="2":
    texto = a[0][0]+" / "+a[1][0]+" = " +str(int(a[0][0])/int(a[1][0]))
else:
    texto = a[0][0]+" - "+a[1][0]+" = " +str(int(a[0][0])-int(a[1][0]))
api.update_status(status=texto)
if a[1]=="1000":
    if a[2]=="3":
        a[2]="0"
        a[0]=str(int(a[0]) + 1) + '\n'
    else:
        a[2] = str(int(a[2])+1)
    a[1]==0
else:
    a[1] = str(int(a[1]) + 1) + '\n'

with open('a.txt', 'w') as file:
    file.writelines(a)
