from random import randint

#Get the data
user_name = input("Intro the Name of User: ")
lastname_user = input("Intro the Lastname User: ")
born_year = input("Intro the Born of Year (yyyy): ")
while len(born_year) < 4:
    born_year = input("Intro the Born of Year: ")
random_id = randint(1000,9999)

#Normalize data
normalize_user_name = user_name.strip().upper()[0:2]
normalize_lastname_user = lastname_user.strip().upper()[0:2]
normalize_born_year = born_year.strip()[2:]
normalize_random_id = str(random_id)

#generate the ID
user_id = normalize_user_name + normalize_lastname_user + normalize_born_year + normalize_random_id

#show the result
print()
print(f'The userID generated are: {user_id}')
