#sentence if
from random import randint
from random import randrange

print("************* Sentence if ************")

print('\nExercise 1')

age = input('Intro the age: ')

if int(age) < 18:
    print(f"You are a boy, have {age} years")
elif int(age) < 60:
    print(f"You are a adult, have {age} years")
else:
    print(f"You are a old man, have {age} years")

print('\nexercise 2')
ran = randint(0, 100)

if ran > 50:
    print(f'The random ({ran}) is mayor to 50')
else:
    print(f'The random ({ran}) is minor to 50')

print('\nExercise 3')
salary = randrange(1000, 5000)
if salary < 3000:
    print(f'you are a employed {salary}')
elif salary < 4000:
    print(f'You are a in charge {salary}')
elif salary < 4500:
    print(f'You are a boss {salary}')
else:
    print(f'You are the owner {salary}')

