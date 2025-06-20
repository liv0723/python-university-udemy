name = "Ubaldo Acosta Soto"
company = 'Global Mentoring'
domain = 'com.mx'

normalize_name = '.'.join(name.strip().lower().split())
normalize_company = company.strip().lower().replace(' ', '')
normalize_domain = f'.{domain}'

email = normalize_name + '@' + (normalize_company + normalize_domain)

print("---------- Email Challenger -----------", "\n")

print(f"Name Employed: {name}")
print("Name Company: ", company)
print("Domain: " + normalize_domain)

print(f"\nEmail: {normalize_name + '@' + normalize_company + normalize_domain}")

