import requests
import json
from lxml import html
from bs4 import BeautifulSoup

#checks if an email has an about.me acccount associated with it and returns a link to the profile
def email2aboutme(email):

	

	session = requests.Session()

	try:
		response=session.get("https://about.me/login")

		soup = BeautifulSoup(response.content, 'html.parser')
		AUTH_TOKEN = json.loads( soup.find('script','contextData').text )['globals']['AUTH_TOKEN']


		response=session.post("https://about.me/n/password/find_account",data={'email_address': email},headers={'X-Auth-Token':AUTH_TOKEN}).json()

	
		if 'user_name' in response:
			accounts=["https://about.me/" + response['user_name']]
			response=requests.get(accounts[0])
			soup = BeautifulSoup(response.content, 'html.parser')
			for link in soup.find_all('a',class_='social-link'):
				accounts.append(link.get('href'))
			
			return accounts
		else:
			return []
	
	except:
		print("[=]Warning:Something went wrong while attempting to scrap about.me")
		return []



