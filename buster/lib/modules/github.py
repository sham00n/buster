import json


def email2github(email,response):

	try:
		if response.status_code==200:
			data=response.json()
			if data['items'] != []:
				return data['items'][0]['html_url']
			else:
				return ""
		else:
			return ""

	except:
		print("[=]Warning:Something went wrong while attempting to scrap github.com")
		return ""


