import requests
from bs4 import BeautifulSoup


def email2domains(email):

	domain_list=[]
  	
	try:
		response= requests.get("https://domaineye.com/reverse-whois/" + email)
	
		
		soup = BeautifulSoup(response.content, 'html.parser')
		results = soup.find("div",['queryResults', 'all'])

		for column in results.find_all("div",class_="column"):
			for domain in column.find_all("a"):
				domain_list.append(domain.text)
	except:
		print("[=]Warning:you have reached your daily limit for domaineye.com,results that follow this warning wont have domains registered info")

	return domain_list

