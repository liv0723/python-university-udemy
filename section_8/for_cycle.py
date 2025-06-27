#For cycle

print("**************** For Cycle ****************")

msg = input("Intro the message: ")

for var in msg:
    print(var, end='-')

print()
fruits  = ['Apple', 'Banana', 'Mango']

for fruit in fruits:
    print(fruit, end=' ')


notes = [1, 2, 3, 4]
sum = 0

for note in notes:
    sum += note

print()
print(f'The sum of the notes is: {sum}')
print(f'The average of the notes is: {sum / len(notes)} ')



