import pkg_resources
import json

def email2breachedaccts(email,response):

	accounts=[]
	breaches=[]

	with open(pkg_resources.resource_filename('data', 'domain_list.json'),'r') as json_file:
		domains = json.loads(json_file.read())

	if response.status_code==200:
		data=response.json()["value"]
		for breach in data:
			if breach["domain"] != "" and breach["username"] != email :
				if breach["domain"] in domains:
					accounts.append(domains[breach["domain"]].replace('{}',breach["username"]))
				else:
					accounts.append(breach["domain"] + " : " + breach["username"])
			if breach["domain"] != "":
				breaches.append(breach["domain"])
				
	breaches = list(dict.fromkeys(breaches))
	accounts.sort(key=len,reverse=True)


	return {'accounts':accounts,'breaches':breaches}

