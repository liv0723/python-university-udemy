#Challenger range
from pickle import FALSE

MIN_RANGE = 0
MAX_RANGE = 5

value = int(input("Intro the value: "))

if value > MIN_RANGE and value < MAX_RANGE:
    print(f"The value intro is: {True}")
else:
    print(f"The value intro is: {False}")
