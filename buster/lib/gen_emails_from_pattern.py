import pkg_resources
import itertools
import json


#check if a string matches a pattern
def matches_pattern(string,pattern):
	nb=0
	dict={}
	if (len(pattern)==len(string.rstrip())):
		for i in range(0,len(pattern)):
			if pattern[i]!='*':
				dict[i]=pattern[i]
		for i in dict:
			if (dict[i]==string[i]):
				nb=nb+1
		if(nb==len(dict)):
			return True
		else:
			return False
	else:
		return False


#generate emails from personal information and email pattern
def gen_emails_from_pattern(input_info,email_pattern):
	#split email in to 2 parts
	splitAddress = email_pattern.split('@')
	user_pattern=str(splitAddress[0])
	domain_pattern = str(splitAddress[1])


	additional_info=['.','.','_','_']
	#parse current info to generate additional info
	for i in input_info:

		if(i=="first" and len(input_info[i][0])>=2):
			input_info[i].append(input_info[i][0][0])
		elif(i=="last" and len(input_info[i][0])>=4 ):
			input_info[i].append(input_info[i][0][0:1])
			input_info[i].append(input_info[i][0][0:2])
			input_info[i].append(input_info[i][0][0:3])
			input_info[i].append(input_info[i][0][0:4])
		elif(i=="middle" and len(input_info[i][0])>=2):
			input_info[i].append(input_info[i][0][0])
		elif(i=="birthdate"):
			input_info[i][0]=input_info[i][0].replace('*','')
			yyyy=input_info[i][0][-4:]
			yy=input_info[i][0][-2:]	
			input_info[i].append(yy)
		
			if(len(input_info[i][0])==8):
				dd=input_info[i][0][0:2]
				mm=input_info[i][0][2:4]
				input_info[i].append(dd)
				input_info[i].append(mm)
				input_info[i].append(dd + mm + yy)
				input_info[i].append(dd + mm)
				input_info[i].append(yyyy)

				if(dd[0]=='0' and mm[0]!='0'):
					input_info[i].append(dd.replace('0',''))
					input_info[i].append(dd.replace('0','') + mm + yy)
					input_info[i].append(dd.replace('0','') + mm + yyyy)
					input_info[i].append(dd.replace('0','') + mm)
				elif(mm[0]=='0' and dd[0]!='0'):
					input_info[i].append(mm.replace('0',''))
					input_info[i].append(dd + mm.replace('0','') + yy)
					input_info[i].append(dd + mm.replace('0','') + yyyy)
					input_info[i].append(dd + mm.replace('0',''))
				elif(mm[0]=='0' and dd[0]=='0'):
					input_info[i].append(dd.replace('0',''))
					input_info[i].append(mm.replace('0',''))
					input_info[i].append(dd.replace('0','') + mm.replace('0','') + yy)
					input_info[i].append(dd.replace('0','') + mm.replace('0','') + yyyy)
					input_info[i].append(dd.replace('0','') + mm.replace('0',''))
		elif(i=="additional_info"):
			additional_info=additional_info + input_info[i]
			
			


	#generate possible user list from user pattern and available info
	user_list=[]
	for combination in itertools.product(*[ v for v in input_info. values() ]):
		comb=(list(combination))
		comb.extend(additional_info)
		for i in range(2,7):
			permutations=list(itertools.permutations(comb,i))

			for p in permutations:
				user=""
				for i in p:
					user=user+i
				if (matches_pattern(user,user_pattern) and (".." not in user) and ("__" not in user) and ("._" not in user) and  ("_." not in user)  and (user.endswith('.')==False) and (user.endswith('_')==False)):
					user_list.append(user)


	#remove duplicates
	user_list = list(dict.fromkeys(user_list))


	#generate possible domain list from a domain pattern
	domain_list=[]		
	with open( pkg_resources.resource_filename('data', 'email-providers.json'),'r') as json_file:
		domains = json.loads(json_file.read())
		for domain in domains:
			if (matches_pattern(domain,domain_pattern)):
				domain_list.append(domain.rstrip())


	#reconstruct emails from user list and domain list
	email_list=[]
	if(domain_list != [] and user_list != []):
		for domain in domain_list:
			for user in user_list:
				email_list.append(user + '@' + domain)
		return email_list

	elif(domain_list == []):
		print("we couldnt find the email provider in our database,if you know it pass it with the -p option")

		return

	elif(user_list == []):

		print("we couldnt find any email that matches the pattern you provided,try adding more info with the -a option")

		return



