import requests
from validate_email import validate_email



def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


#generate work email from first name,last name and company domain
#returns the email with information associated to it

def gen_work_email(first,last,domain,api_key):
	work_email_info={}
	headers = {'User-Agent': 'Buster - email generation and validation tool'}
	
	if api_key=="":
		response = requests.get("https://hunter.io/trial/v2/email-finder?domain=" + domain + "&first_name=" + first + "&last_name=" + last,headers=headers)
	else:
		response= requests.get("https://api.hunter.io/v2/email-finder?domain=" + domain + "&first_name=" + first + "&last_name=" + last + "&api_key=" + api_key)
	#print(response.status_code)
	if response.status_code == 200:
		data=response.json()
		work_email=data["data"]["email"]

		if(data["data"]["position"] !=None):
			work_email_info["position"]=data["data"]["position"]
		if(data["data"]["twitter"] != None):
			work_email_info["twitter"]="https://www.twitter.com/" + data["data"]["twitter"]
		if(data["data"]["linkedin_url"] != None):
			work_email_info["linkedin"]=data["data"]["linkedin_url"]
		if(data["data"]["phone_number"] != None):
			work_email_info["phone_number"]=data["data"]["phone_number"]
		

		info=merge_two_dicts(work_email_info,validate_email(work_email,api_key))
	else:
		info={"hunter_limit_reached":True}

	return info

	

