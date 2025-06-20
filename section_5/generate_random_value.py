from random import randint
from random import random


generated_value_int = randint(0,10)
generated_value_float = random()
die_number = randint(1,7)

print(f'Generated value between 0-10: {generated_value_int}')
print(f'Generated value between 0-1: {generated_value_float.__round__(2)}')
print(f'The die number: {die_number}')



