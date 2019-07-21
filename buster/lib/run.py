from .validate_email import validate_email
from .gen_work_email import gen_work_email
from .gen_emails_from_info import gen_emails_from_info
from .gen_emails_from_pattern import gen_emails_from_pattern
from .gen_emails_from_username import gen_emails_from_username

import pkg_resources
import argparse
import json
import yaml
import sys
import os
import re



def print_info(email_info):
	if(email_info["exists"]==True):
		print("[+]" + email_info["email"])
		for i in email_info:
			if(i=="profiles"):
				print("\t[-]Profiles:")
				for profile in email_info["profiles"]:
					print("\t\t"+profile)
			elif(i=="sources"):
				print("\t[-]Sources:")
				for source in email_info["sources"]:
					print("\t\t"+source)
			elif(i=="accounts"):
				print("\t[-]Accounts:")
				for account in email_info["accounts"]:
					print("\t\t"+account)
			elif(i=="twitter"):
				print("\t"+email_info["twitter"])
			elif(i=="domains_registered"):
				print("\t[-]Domains registered:")
				for domain in email_info["domains_registered"]:
					print("\t\t"+domain)
			elif(i=="phone_number"):
				print("\t[-]Phone Number:")
				print("\t"+email_info["phone_number"])
			elif(i=="position"):
				print("\t[-]Position:")
				print("\t"+email_info["position"])
			elif(i=="breaches"):
				print("\t[-]Breaches:")
				for breach in email_info["breaches"]:
					print("\t\t"+breach)
			elif(i=="pastes"):
				print("\t[-]Pastes:")
				for paste in email_info["pastes"]:
					print("\t\t"+paste)
					


def start():
	parser = argparse.ArgumentParser(description='Buster is an OSINT tool used to generate and verify emails and return information associated with them')
	parser.add_argument('-e', '--email', help='email adress or email pattern',type=str)
	parser.add_argument('-f', '--first', help='first name',type=str)
	parser.add_argument('-m', '--middle', help='middle name',type=str)
	parser.add_argument('-l', '--last', help='last name', type=str)
	parser.add_argument('-b', '--birthdate', help='birthdate in ddmmyyyy format,type * if you dont know(ex:****1967,3104****)',type=str)
	parser.add_argument('-a', '--addinfo', help='additional info to help guessing the email(ex:king,345981)',nargs='+')
	parser.add_argument('-u', '--username', help='checks 100+ email providers for the availability of username@provider.com',type=str)
	parser.add_argument('-c', '--company', help='company domain',type=str)
	parser.add_argument('-p', '--providers', help='email provider domains',nargs='+')
	parser.add_argument('-o', '--output', help='output to a file',type=str)
	parser.add_argument('-v','--validate', help='check which emails are valid and returns information of each one',action='store_true')
	parser.add_argument('--list', help='file containing list of emails',type=str)
    
	args = parser.parse_args()
	
	
	
	
	with open( pkg_resources.resource_filename('data', 'api-keys.yaml'), 'r') as api_keys:
            keys = yaml.safe_load(api_keys)

	api_key=str(keys['apikeys']['hunter']['key'])
	
	
	if(args.output):
		
		sys.stdout = open(args.output, 'w+')

	
	if(args.email and args.first and args.middle and args.last and args.birthdate and('*' in args.email)):
		if args.addinfo:
			input_info={"first":[args.first],"middle":[args.middle],"last":[args.last],"birthdate":[args.birthdate],"additional_info":args.addinfo}
		else:
			input_info={"first":[args.first],"middle":[args.middle],"last":[args.last],"birthdate":[args.birthdate]}
	
		generated_emails=gen_emails_from_pattern(input_info,args.email)

		if(generated_emails != []):
			print("[=]Validating " + str(len(generated_emails)) + " possible emails")
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)


	elif(args.email and args.first and args.middle and args.last and('*' in args.email)):
		if args.addinfo:
			input_info={"first":[args.first],"middle":[args.middle],"last":[args.last],"additional_info":args.addinfo}
		else:
			input_info={"first":[args.first],"middle":[args.middle],"last":[args.last]}
	
		generated_emails=gen_emails_from_pattern(input_info,args.email)

		if(generated_emails != []):
			print("[=]Validating " + str(len(generated_emails)) + " possible emails")
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)


	elif(args.email and args.first and args.last and args.birthdate and('*' in args.email)):
		if args.addinfo:
			input_info={"first":[args.first],"last":[args.last],"birthdate":[args.birthdate],"additional_info":args.addinfo}
		else:
			input_info={"first":[args.first],"last":[args.last],"birthdate":[args.birthdate]}
	
		generated_emails=gen_emails_from_pattern(input_info,args.email)

		if(generated_emails != []):
			print("[=]Validating " + str(len(generated_emails)) + " possible emails")
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)


	elif(args.email and args.first and args.last):
		if args.addinfo:
			input_info={"first":[args.first],"last":[args.last],"additional_info":args.addinfo}
		else:
			input_info={"first":[args.first],"last":[args.last]}
	
		generated_emails=gen_emails_from_pattern(input_info,args.email)
	
		print("[=]Validating " + str(len(generated_emails)) + " possible emails")
		if(generated_emails != []):
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)


	elif(args.email and ('*' not in args.email)):
		email_info=validate_email(args.email)
		if(email_info["emailrep_limit_reached"]==False and email_info["exists"]==True):
			print_info(email_info)
		elif(email_info["emailrep_limit_reached"]==False and email_info["exists"]==False):
			print("[=]No Info was found on the email address " + args.email )

		else:
			print("[=]You have reached your daily limit")
			exit(1)



	elif(args.first and args.last and args.company):
		email_info=gen_work_email(args.first,args.last,args.company,api_key)
		if("hunter_limit_reached" in email_info ):
			print("[=]Error:You have reached your Hunter.io usage limit")
			print("[=]Use an API key if you want to use this option")
		else:
			if(email_info["emailrep_limit_reached"]==False and email_info["exists"]==True):
				print_info(email_info)
			elif(email_info["emailrep_limit_reached"]==True):
				print("[=]You have reached your daily limit")
				exit(1)
			elif(email_info["exists"]==False):
				print("[=]We were unable to find a person with this name working for this company")


	elif(args.first and args.middle and args.last and args.birthdate):
		input_info={"first":args.first,"middle":args.middle,"last":args.last,"birthdate":args.birthdate}
		if(args.providers):
			generated_emails=gen_emails_from_info(input_info,args.providers)
			if(args.validate):
				for email in generated_emails:
					email_info=validate_email(email)
					if(email_info["emailrep_limit_reached"]==False):
						print_info(email_info)
					else:
						print("[=]You have reached your daily limit")
						exit(1)
			else:
				print("[=]Generated emails:")
				for email in generated_emails:
					print(email + "\n")
		else:
			generated_usernames=gen_emails_from_info(input_info,[])
			print("[=]Generated usernames:")
			for username in generated_usernames:
				print(username + "\n")


	elif(args.first and args.middle and args.last):
		input_info={"first":args.first,"middle":args.middle,"last":args.last}
		if(args.providers):
			generated_emails=gen_emails_from_info(input_info,args.providers)
			if(args.validate):
				for email in generated_emails:
					email_info=validate_email(email)
					if(email_info["emailrep_limit_reached"]==False):
						print_info(email_info)
					else:
						print("[=]You have reached your daily limit")
						exit(1)
			else:
				print("[=]Generated emails:")
				for email in generated_emails:
					print(email + "\n")
		else:
			generated_usernames=gen_emails_from_info(input_info,[])
			print("[=]Generated usernames:")
			for username in generated_usernames:
				print(username + "\n")


	elif(args.first and args.last and args.birthdate):
		input_info={"first":args.first,"last":args.last,"birthdate":args.birthdate}
		if(args.providers):
			generated_emails=gen_emails_from_info(input_info,args.providers)
			if(args.validate):
				for email in generated_emails:
					email_info=validate_email(email)
					if(email_info["emailrep_limit_reached"]==False):
						print_info(email_info)
					else:
						print("[=]You have reached your daily limit")
						exit(1)
			else:
				print("[=]Generated emails:")
				for email in generated_emails:
					print(email + "\n")
		else:
			generated_usernames=gen_emails_from_info(input_info,[])
			print("[=]Generated usernames:")
			for username in generated_usernames:
				print(username + "\n")


	elif(args.first and args.last):
		input_info={"first":args.first,"last":args.last}
		if(args.providers):
			generated_emails=gen_emails_from_info(input_info,args.providers)
			if(args.validate):
				for email in generated_emails:
					email_info=validate_email(email)
					if(email_info["emailrep_limit_reached"]==False):
						print_info(email_info)
					else:
						print("[=]You have reached your daily limit")
						exit(1)
			else:
				print("[=]Generated emails:")
				for email in generated_emails:
					print(email + "\n")
		else:
			generated_usernames=gen_emails_from_info(input_info,[])
			print("[=]Generated usernames:")
			for username in generated_usernames:
				print(username + "\n")

	

	elif(args.username and args.providers):
		generated_emails=gen_emails_from_username(args.username,args.providers)
		if(generated_emails != []):
			print("[=]Validating " + str(len(generated_emails)) + " possible emails")
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)
			
	elif(args.username):
		domain_list=[]		
		with open( pkg_resources.resource_filename('data', 'email-providers.json'),'r') as json_file:
			domains = json.loads(json_file.read())
			for domain in domains:
				domain_list.append(domain)

		generated_emails=gen_emails_from_username(args.username,domain_list)
		if(generated_emails != []):
			print("[=]Validating " + str(len(generated_emails)) + " possible emails")
			for email in generated_emails:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)
		

	


	elif(args.list):
		with open(args.list,'r') as f:
			emails = f.readlines()
			emails = [x.rstrip() for x in emails]
		for email in emails:
			if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$', email) != None:
				email_info=validate_email(email)
				if(email_info["emailrep_limit_reached"]==False):
					print_info(email_info)
				else:
					print("[=]You have reached your daily limit")
					exit(1)


	else:
		print (parser.print_help())
				








	
