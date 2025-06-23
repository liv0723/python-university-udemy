#Authentication System

PASSWORD = 'xxx'
USER = 'xxx'

print("******** System Authentication *********")
user = input("Intro the user: ")
password = input("Intro the password: ")

comparison_user = (USER == user)
comparison_pass = (PASSWORD == password)

if comparison_user and comparison_pass:
    print("The authentication is fine:")
else:
    print("The authentication is not fine")






