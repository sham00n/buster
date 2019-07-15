
#generate emails from personal info if domains are specified,generates usernames if not

def gen_emails_from_info (input_info,input_domains):
	user_list=[]
	if("first" in input_info and "last" in input_info):
		user_list.append(input_info["first"] + input_info["last"])
		user_list.append(input_info["first"] + "." + input_info["last"])
		user_list.append(input_info["first"] + "_" + input_info["last"])

	if("first" in input_info and "middle" in input_info and "last" in input_info):
		user_list.append(input_info["first"] + input_info ["middle"] + input_info["last"])
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"])
		user_list.append(input_info["first"] + "." + input_info ["middle"][0] + "." + input_info["last"])
		user_list.append(input_info["first"] + "_" + input_info ["middle"][0] + "_" + input_info["last"])
	
	 
	if("first" in input_info and "birthdate" in input_info and "last" in input_info):
		birthdate=input_info["birthdate"].replace('*','')
		yyyy=input_info["birthdate"][-4:]
		yy=input_info["birthdate"][-2:]
		
		user_list.append(input_info["first"] + input_info["last"] + yyyy)
		user_list.append(input_info["first"] + input_info["last"] + "." + yyyy)
		user_list.append(input_info["first"] + input_info["last"] + "_" + yyyy)
		user_list.append(input_info["first"] + input_info["last"] + yy)
		user_list.append(input_info["first"] + input_info["last"] + "." + yy)
		user_list.append(input_info["first"] + input_info["last"] + "_" + yy)
		user_list.append(input_info["first"] + "." + input_info["last"] + "." + yyyy)
		user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + yyyy)
		user_list.append(input_info["first"] + "." + input_info["last"] + "." + yy)
		user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + yy)
		
		user_list.append(input_info["first"][0] + input_info["last"] + yyyy)
		user_list.append(input_info["first"][0] + input_info["last"] + "." + yyyy)
		user_list.append(input_info["first"][0] + input_info["last"] + "_" + yyyy)
		user_list.append(input_info["first"][0] + input_info["last"] + yy)
		user_list.append(input_info["first"][0] + input_info["last"] + "." + yy)
		user_list.append(input_info["first"][0] + input_info["last"] + "_" + yy)
		user_list.append(input_info["first"][0] + "." + input_info["last"] + "." + yyyy)
		user_list.append(input_info["first"][0] + "_" + input_info["last"] + "_" + yyyy)
		user_list.append(input_info["first"][0] + "." + input_info["last"] + "." + yy)
		user_list.append(input_info["first"][0] + "_" + input_info["last"] + "_" + yy)

		user_list.append(input_info["first"] + input_info["last"][0] + yyyy)
		user_list.append(input_info["first"] + input_info["last"][0] + "." + yyyy)
		user_list.append(input_info["first"] + input_info["last"][0] + "_" + yyyy)
		user_list.append(input_info["first"] + input_info["last"][0] + yy)
		user_list.append(input_info["first"] + input_info["last"][0] + "." + yy)
		user_list.append(input_info["first"] + input_info["last"][0] + "_" + yy)
		user_list.append(input_info["first"] + "." + input_info["last"][0] + "." + yyyy)
		user_list.append(input_info["first"] + "_" + input_info["last"][0] + "_" + yyyy)
		user_list.append(input_info["first"] + "." + input_info["last"][0] + "." + yy)
		user_list.append(input_info["first"] + "_" + input_info["last"][0] + "_" + yy)

		if (len(birthdate)==8):
			dd=(input_info["birthdate"][0:2]).replace('0','')
			mm=(input_info["birthdate"][2:4]).replace('0','')
			
			user_list.append(input_info["first"] + input_info["last"] + mm)
			user_list.append(input_info["first"] + input_info["last"] + "." + mm)
			user_list.append(input_info["first"] + input_info["last"] + "_" + mm)
			user_list.append(input_info["first"] + input_info["last"] + dd)
			user_list.append(input_info["first"] + input_info["last"] + "." + dd)
			user_list.append(input_info["first"] + input_info["last"] + "_" + dd)
			user_list.append(input_info["first"] + "." + input_info["last"] + "." + mm)
			user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + mm)
			user_list.append(input_info["first"] + "." + input_info["last"] + "." + dd)
			user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + dd)
		
			user_list.append(input_info["first"][0] + input_info["last"] + mm)
			user_list.append(input_info["first"][0] + input_info["last"] + "." + mm)
			user_list.append(input_info["first"][0] + input_info["last"] + "_" + mm)
			user_list.append(input_info["first"][0] + input_info["last"] + dd)
			user_list.append(input_info["first"][0] + input_info["last"] + "." + dd)
			user_list.append(input_info["first"][0] + input_info["last"] + "_" + dd)
			user_list.append(input_info["first"][0] + "." + input_info["last"] + "." + mm)
			user_list.append(input_info["first"][0] + "_" + input_info["last"] + "_" + mm)
			user_list.append(input_info["first"][0] + "." + input_info["last"] + "." + dd)
			user_list.append(input_info["first"][0] + "_" + input_info["last"] + "_" + dd)

			user_list.append(input_info["first"] + input_info["last"][0] + mm)
			user_list.append(input_info["first"] + input_info["last"][0] + "." + mm)
			user_list.append(input_info["first"] + input_info["last"][0] + "_" + mm)
			user_list.append(input_info["first"] + input_info["last"][0] + dd)
			user_list.append(input_info["first"] + input_info["last"][0] + "." + dd)
			user_list.append(input_info["first"] + input_info["last"][0] + "_" + dd)
			user_list.append(input_info["first"] + "." + input_info["last"][0] + "." + mm)
			user_list.append(input_info["first"] + "_" + input_info["last"][0] + "_" + mm)
			user_list.append(input_info["first"] + "." + input_info["last"][0] + "." + dd)
			user_list.append(input_info["first"] + "_" + input_info["last"][0] + "_" + dd)

			user_list.append(input_info["first"] + input_info["last"] + dd + mm)
			user_list.append(input_info["first"] + input_info["last"] + "." + dd + mm)
			user_list.append(input_info["first"] + input_info["last"] + "_" + dd + mm)
			user_list.append(input_info["first"] + input_info["last"] + dd + mm)
			user_list.append(input_info["first"] + input_info["last"] + "." + dd + mm)
			user_list.append(input_info["first"] + input_info["last"] + "_" + dd + mm)
			user_list.append(input_info["first"] + "." + input_info["last"] + "." + dd + mm)
			user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + dd + mm)
			user_list.append(input_info["first"] + "." + input_info["last"] + "." + dd + mm)
			user_list.append(input_info["first"] + "_" + input_info["last"] + "_" + dd + mm)
			

	if("first" in input_info and "middle" in input_info and "last" in input_info and "birthdate" in input_info):
		yyyy=input_info["birthdate"][-4:]
		yy=input_info["birthdate"][-2:]

		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + yyyy)
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + "." + yyyy)
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + "_" + yyyy)
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + yy)
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + "." + yy)
		user_list.append(input_info["first"] + input_info ["middle"][0] + input_info["last"] + "_" + yy)


	email_list=[]
	for domain in input_domains:
		for user in user_list:
			email_list.append(user + '@' + domain)
	
	if(input_domains == []):	
		return user_list
	else:
		return email_list





