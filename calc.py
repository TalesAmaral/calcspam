import tweepy
consumer_secret = ""
consumer_key = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.API(auth)
tweet = client.user_timeline(id = client.me().id, count = 1)[0].text
i = int(tweet[57:len(tweet)])+1
while True:
	texto = "Eu quero jogar street fighter ou tekken... pedido número "+str(i)
	api.update_status(status=texto)
	i+=1
