#Form Validation

print("*********** Form Validation *************")
USER_NAME = 'pepe'
USER_PASS = "pepe"

user_name = None
user_pass = None

while (not user_name) or (not user_pass):
    user_name = input("Intro the user name: ")
    user_pass = input("Intro the pass: ")

    if user_name == USER_NAME :
        if user_pass == USER_PASS:
            print("Congratulations ...")
        else:
            print("The Pass is wrong")
    else:
        print("The User is wrong ")





