import requests
from bs4 import BeautifulSoup
import re


#get sources from a google search of the email

def google_search(email):
	email_sources=[]
	
	try:
		response = requests.get('https://www.google.com/search?q=intext:' + email)
		soup = BeautifulSoup(response.content,features="lxml")
		links = soup.findAll("a")
		sources=[]
		for source in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
			sources.append(re.split(":(?=http)",source["href"].replace("/url?q=","")) )
			
	
		for source in sources:
			if("google.com" not in source[0]):
						
				email_sources.append(str(source[0].split('&')[0]).replace("%3D","=").replace("%3F","?"))

		if(len(email_sources)!=0):
			email_sources = list(dict.fromkeys(email_sources))
	except:
		print("[=]Warning:Something went wrong while attempting to scrap google.com")
	
	return email_sources


