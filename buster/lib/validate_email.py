import grequests
import json

from .modules.hibp_pastes import email_pastes
from .modules.domaineye import email2domains
from .modules.gravatar import email2gravatar
from .modules.linkedin import email2linkedin
from .modules.aboutme import email2aboutme
from .modules.myspace import email2myspace
from .modules.github import email2github
from .modules.skype import email2skype
from .modules.avast import email2breachedaccts
from .modules.twitter import twitter_search
from .modules.darksearch import dark_search
from .modules.googledork import google_search
#from .modules.flickr import email2flickr


def validate_email(email):
	email_info={"email":email,"exists":False,"emailrep_limit_reached":False}
	headers = {'User-Agent': 'Buster - email OSINT tool'}

	accounts=[]
	sources=[]

	reqs = [
		  grequests.get("https://emailrep.io/" + email),
		  grequests.get("https://myspace.com/search/people?q=" + email),
		  grequests.get("https://api.github.com/search/users?q=" + email + "+in:email"),
		  grequests.get('https://darksearch.io/api/search?query="' + email + '"'),
		  grequests.get("https://haveibeenpwned.com/api/v2/pasteaccount/" + email,headers=headers),
		  grequests.post("https://digibody.avast.com/v1/web/leaks",json={"email":email})
		]

	response=grequests.map(reqs)

	if response[0].status_code == 200:
		data = response[0].json()
		if(data["details"]["deliverable"]==True):
			email_info["exists"]=True
			
		if(data["details"]["last_seen"]!="never"):
			email_info["exists"]=True

		
		if(data["details"]["profiles"]!=[]):
			email_info["exists"]=True
			email_info["profiles"]=data["details"]["profiles"]
			if "gravatar" in email_info["profiles"]:
				gravatar=email2gravatar(email)
				if gravatar != []:
					accounts.extend(gravatar)
			if "aboutme" in email_info["profiles"]:
				aboutme=email2aboutme(email)
				if aboutme != []:
					accounts.extend(aboutme)
			if "linkedin" in email_info["profiles"]:
				accounts.append(email2linkedin(email))
		
			
		

		myspace=email2myspace(email,response[1])
		if(myspace != []):
			email_info["exists"]=True
			accounts.extend(myspace)

		github=email2github(email,response[2])
		if(github != ""):
			email_info["exists"]=True
			accounts.append(github)
	
		darksearch_sources=dark_search(email,response[3])
		if(darksearch_sources != []):
			email_info["exists"]=True
			sources.extend(darksearch_sources)
		
		
		pastes=email_pastes(email,response[4])
		if(pastes != []):
			email_info["exists"]=True
			email_info["pastes"]=pastes

		breached_accts=email2breachedaccts(email,response[5])
		if(breached_accts["accounts"] != []):
			email_info["exists"]=True
			accounts.extend(breached_accts["accounts"])

		if(breached_accts["breaches"] != []):
			email_info["exists"]=True
			email_info["breaches"]=breached_accts["breaches"]
			

		if(email_info["exists"]==True):
			
			skype=email2skype(email)
			if(skype != []):
				accounts.extend(skype)

			#flickr=email2flickr(email)
			#if(flickr != ""):
				#accounts.append(flickr)

			google_sources=google_search(email)
			if(google_sources != []):
				sources.extend(google_sources)

			twitter_sources=twitter_search(email)
			if(twitter_sources != []):
				sources.extend(twitter_sources)
			
			domains_registered=email2domains(email)
			if(domains_registered != []):
				email_info["domains_registered"]=domains_registered

		if accounts != []:
			email_info["accounts"] = accounts
		if sources != []:
			email_info["sources"] = sources
					

	else:
		email_info["emailrep_limit_reached"]=True
	

	return email_info

