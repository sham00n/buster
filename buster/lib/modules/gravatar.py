import hashlib
import requests

#checks if an email has a gravatar acccount associated with it and returns a link to the profile
def email2gravatar(email):
	email_hash=hashlib.md5(email.encode('utf-8')).hexdigest()
	
	
	
	try:
		response=requests.get("https://www.gravatar.com/" + email_hash)
		if response.status_code==200:
			return response.url
		else:
			return ""
	except:
		print("[=]Warning:Something went wrong while attempting to scrap gravatar.com")
		return ""
	

