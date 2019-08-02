import hashlib
import requests
import json

#checks if an email has a gravatar acccount associated with it and returns a link to the profile
def email2gravatar(email):
	email_hash=hashlib.md5(email.encode('utf-8')).hexdigest()
	
	accounts=[]
	
	try:
		response=requests.get("https://www.gravatar.com/" + email_hash)
		
		if response.status_code==200:
			accounts.append(response.url)
			response=requests.get(response.url + '.json')
			urls=response.json()['entry'][0]['urls']
			for url in urls:
				accounts.append(url['value'])

	except:
		print("[=]Warning:Something went wrong while attempting to scrap gravatar.com")

	return accounts	

