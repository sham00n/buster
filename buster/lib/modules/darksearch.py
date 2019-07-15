import json



def dark_search(email,response):	
	sources=[]
	
	try:
		if response.status_code==200:
			results=response.json()['data']
			for result in results:
				sources.append(result['link'])
	except:
		print("[=]Warning:Something went wrong while attempting to scrap darksearch.io")
		
		
	return sources



