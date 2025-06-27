#Password

print("*************** Password ****************")

password = input("Intro the password: ")

while len(password) < 6:
    new_character = input("Intro the more character: ")
    password += new_character
else:
    print("Congratulations !!!")

