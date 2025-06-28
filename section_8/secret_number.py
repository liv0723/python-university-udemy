#Secret Number
from random import randint

print("*************** Secret NUmber ***************")

secret_number = randint(0, 5)
numbers_attempts = 0

print(secret_number)
user_number = int(input("Intro de number: ").strip())

while numbers_attempts < 5 :

    if user_number != secret_number:
        if user_number > secret_number:
            user_number = int(input("The number was mayor: ").strip())
        else:
            user_number = int(input("The number was minor: ").strip())
        numbers_attempts += 1
    else:
        print(f'Congratulation, used {numbers_attempts} attempts')
        exit()
#else:
#    print(f'You failed used {numbers_attempts} attempts')
