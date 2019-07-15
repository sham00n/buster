import requests
from bs4 import BeautifulSoup
from lxml import html


																																																																																				
def email2skype(email):
	url="https://webresolver.nl/ajax/tools/email2skype"
	data = {"string":email,"action":"PostData"}
	headers={'Referer':'https://webresolver.nl/tools/email_to_skype','X-Requested-With':'XMLHttpRequest'}

	try:
		response=requests.get("https://webresolver.nl/tools/email_to_skype")
		soup = BeautifulSoup(response.content, 'html.parser')
		token=str(soup.body.script).split('WebResolverSecurityCode=')[1].split('; expires=')[0]	

		cookies = dict(response.cookies)
		cookies['WebResolverSecurityCode']=token

		r = requests.post(url,data=data,headers=headers,cookies=cookies)
		soup = BeautifulSoup(r.content, 'html.parser')

		results = str(soup.div).replace('</div>', '').split('<br/>')[1:]

		if(results != ['An error occoured!'] and results !=['There were no Skype usernames found with this email.']):
			newresults=[]
			for result in results:
				newresults.append("Skype : " + result)
			return newresults
		else:
			return []
	except:
		print("[=]Warning:Something went wrong while attempting to scrap webresolver.com")
		return []



