#Ternary Operator
from random import randint

age = int(input("Intro the age: "))
is_adult = 'Is adult' if age >= 18 else "Isn't adult"
print(is_adult,f'and have {age} years', sep= ' ' )

random = randint(-10, 10)
is_positive = f"\nIs Positive {random}" if random >= 0 else f'Isn\'t Positive {random}'
print(is_positive)
