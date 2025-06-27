#calculator

print("*************** Calculator ***************")

operation = None
result = 0

while operation is None:

    new_operation =  input("""
    1.\tSuma
    2.\tRest
    3.\tMult
    4.\tDiv
    """).strip()

    if new_operation == '1':
        value_1, value_2 = input("Intro the value separate by ' ': ").strip().split()
        result = int(value_1) + int(value_2)
        print(f'The result is : {result}')
        operation = new_operation
    elif new_operation == '2':
        value_1, value_2 = input("Intro the value separate by ' ': ").strip().split()
        result = int(value_1) - int(value_2)
        print(f'The result is : {result}')
        operation = new_operation
    elif new_operation == '3':
        value_1, value_2 = input("Intro the value separate by ' ': ").strip().split()
        result = int(value_1) * int(value_2)
        print(f'The result is : {result}')
        operation = new_operation
    elif new_operation == '4':
        value_1, value_2 = input("Intro the value separate by ' ': ").strip().split()
        result =  int(value_1) / int(value_2)
        print(f'The result is : {result}')
        operation = new_operation
    else:
        print('The operation selected is bad: ')








