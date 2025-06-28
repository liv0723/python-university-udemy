# Triangle  and square

print("********** Triangle and Square ************")

row_number = int(input('Intro the number of row: '))

for fila in range(1,row_number + 1, 1):
    spaces_number =' ' * (row_number - fila)
    print(spaces_number, ('*' * (2 * fila - 1) ), sep='')


square = int(input("Intro the number: "))

for i in range(1, square + 1, 1):
    print('*' * square )


