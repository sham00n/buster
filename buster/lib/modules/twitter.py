import twint

def twitter_search(email):
	
	splitAddress = email.split('@')
	user=str(splitAddress[0])
	domain = str(splitAddress[1].split('.')[0])
	tweets = []
	sources=[]

	try:
		config = twint.Config()
		config.Search = user + ' ' + domain
		config.Store_object = True
		config.Hide_output = True
		config.Limit = 10
	
		config.Store_object_tweets_list = tweets
		twint.run.Search(config)
	
		for tweet in tweets:
			if(user in tweet.tweet and domain in tweet.tweet):
				sources.append(tweet.link)
	except:
		print("[=]Warning:Something went wrong while attempting to scrap twitter.com")

	return sources



