#Authentication System

print("*************** Authentication System ***************")

USER = "pepe"
PASSWORD = "pepe"

user = input("Intro the user: ")
password = input("Intro the password: ")

message = 'Welcome to the System' if (user == USER and password == PASSWORD) else 'Invalid User' if (user != USER and password == PASSWORD) else 'Invalid Pass' if (user == USER and password != PASSWORD) else 'Invalid User and Pass '

print(message)