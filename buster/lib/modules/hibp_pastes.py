import requests
import json



#get pastes of the email from haveibeenpwned.com

def email_pastes(email,response):
	pastes=[]
	try:
		if response.status_code==200:
			data=response.json()
			for paste in data:
				if(paste["Source"]=="Pastebin"):
					pastes.append("https://pastebin.com/" + paste["Id"])
				else:
					pastes.append(paste["Id"])
	except:

		print("[=]Warning:Something went wrong while attempting to scrap haveibeenpwned.com")

	return pastes


