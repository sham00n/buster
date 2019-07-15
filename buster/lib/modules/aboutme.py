import requests
import json
from lxml import html
from bs4 import BeautifulSoup

#checks if an email has an about.me acccount associated with it and returns a link to the profile
def email2aboutme(email):

	url="https://about.me/n/password/find_account"

	session = requests.Session()

	try:
		response=session.get("https://about.me/login")

		soup = BeautifulSoup(response.content, 'html.parser')
		AUTH_TOKEN = json.loads( soup.find('script','contextData').text )['globals']['AUTH_TOKEN']


		response=session.post(url,data={'email_address': email},headers={'X-Auth-Token':AUTH_TOKEN}).json()

	
		if 'user_name' in response:
			return "https://about.me/" + response['user_name']
		else:
			return ""
	
	except:
		print("[=]Warning:Something went wrong while attempting to scrap about.me")
		return ""












