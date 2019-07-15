from lxml import html
from bs4 import BeautifulSoup

#checks if an email has a myspace acccount associated with it and returns a link to the profile
def email2myspace(email,response):
	sources=[]
	
	try:
		soup = BeautifulSoup(response.content, 'html.parser')
		results = soup.find_all("h6")
	
		for result in results:
			if(email in result.text and result.a.has_attr('href')):
				sources.append("https://myspace.com" + result.a.attrs['href'])

	except:
		print("[=]Warning:Something went wrong while attempting to scrap myspace.com")

	
	
	return sources


