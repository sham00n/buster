from bs4 import BeautifulSoup
import requests
import json
import re

def validate_email(email,api_key):
	email_info={"email":email,"exists":False,"hunter_limit_reached":False,"emailrep_limit_reached":False}
	headers = {'User-Agent': 'Buster - email generation and validation tool'}

	response = requests.get("https://emailrep.io/" + email)
	if response.status_code == 200:
		data = response.json()
		if(data["details"]["deliverable"]==True):
			email_info["exists"]=True
	
		if(data["details"]["profiles"]!=[]):
			email_info["exists"]=True
			email_info["profiles"]=data["details"]["profiles"]

		if(data["details"]["credentials_leaked"]==True):
			email_info["exists"]=True

			response = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/" + email + "?truncateResponse=true",headers=headers)
			if response.status_code == 200:
				data = response.json()
				breaches=[]
				for Breach in data:
					breaches.append(Breach['Name'])

				email_info["breaches"]=breaches
		
		#get sources from a google search of the email
		if (email_info["exists"]==True):
			response = requests.get('https://www.google.com/search?q=intext:' + email)
			if response.status_code == 200:
				soup = BeautifulSoup(response.content,features="lxml")
				links = soup.findAll("a")
				sources=[]
				for source in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
					sources.append(re.split(":(?=http)",source["href"].replace("/url?q=","")) )
				
				email_sources=[]
				for source in sources:
					if("https://accounts.google.com/" not in source[0]):
						email_sources.append(str(source[0].split('&')[0]))

				if(len(email_sources)!=0):
					email_sources = list(dict.fromkeys(email_sources))
					email_info["sources"]=email_sources
				
		


		

		#get pastes of the email from haveibeenpwned.com
		if (email_info["exists"]==True):
			
			response=requests.get("https://haveibeenpwned.com/api/v2/pasteaccount/" + email,headers=headers)
			if response.status_code == 200:
				data=response.json()
				pastes=[]
				for paste in data:
					if(paste["Source"]=="Pastebin"):
						pastes.append("https://pastebin.com/" + paste["Id"])
					else:
						pastes.append(paste["Id"])

				email_info["pastes"]=pastes

				

		

	elif response.status_code == 429:
		email_info["emailrep_limit_reached"]=True
	

	return email_info


