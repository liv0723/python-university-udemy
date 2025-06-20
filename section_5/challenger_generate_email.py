from multiprocessing.pool import job_counter

print("******* Challenger Generate EMAIL ********")

#Getting the data
user_name = input("Intro the name of user: ")
user_lastname = input("Intro the Lastname of user: ")
company_name = input("Intro the name of Company: ")
domain_extension = input("Intro the domain starting with a . :")

#Normalize the data
normalize_user_name = user_name.strip().lower().replace(' ', '.')
normalize_user_lastname = user_lastname.strip().lower().replace(' ', '.')
normalize_company_name = company_name.strip().lower().replace(" ",'')
normalize_domain_extension = domain_extension.strip().lower()

#Generate the email
email_user = '.'.join([normalize_user_name, normalize_user_lastname])
email_domain = normalize_company_name + normalize_domain_extension
email = f'{email_user}@{email_domain}'

print(f'The email is: {email}')