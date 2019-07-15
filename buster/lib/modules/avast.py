
def email2breachedaccts(email,response):

	accounts=[]
	breaches=[]

	if response.status_code==200:
		data=response.json()["value"]
		for breach in data:
			if breach["domain"] != "" and breach["username"] != email :
				accounts.append(breach["domain"] + " : " + breach["username"])
			if breach["domain"] != "":
				breaches.append(breach["domain"])


	return {'accounts':accounts,'breaches':breaches}


