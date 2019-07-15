

#generate emails from username

def gen_emails_from_username(username,domains):

	email_list=[]

	for domain in domains:
		email_list.append(username + '@' + domain)

	return email_list


