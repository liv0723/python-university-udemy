#Compund Assignment Operators

num_1, num_2 = input("Intro the number, separate by ' ':").split(' ')

print(f"Number 1 is: {num_1}, Number 2 is: {num_2}")

num_1, num_2 = int(num_1), int(num_2)
operation = input("Intro the operation (sum-rest-mul-div): ")
if operation == 'sum':
    num_1 += num_2
else:
    if operation == 'res':
        num_1 -= num_2
    else:
        if operation == 'mul':
            num_1 *= num_2
        else:
            num_1 /= num_2




print(f"the operation is: {operation}, and the result is: {num_1}")



