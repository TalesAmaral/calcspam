import tweepy
consumer_secret = "GAROC34w8rjQcYVLPoF6RLCnJ9s4V42vUyGD0dSLiwKMjOJ9gd"
consumer_key = "aCEgAQYUD051Rpv81gB5nOdJD"
access_token = "911589205339451392-4e4xIDp9LAgHpkgS6zqtiEpvmSHteHe"
access_token_secret = "pxi7IczC2SObAgxLdTdEYLhcuW02awrW8eXRPFL6c0ybY"
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
