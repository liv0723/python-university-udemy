#Range Function

print("**************** Range Function ***************")

for var in range(1,50,2):
    print(var, end='-')

print()
for var in range(0,50, 2):
    print(var, end= '-')

print()
msg = input('Intro the msg to show: ')
quantity = int(input("Intro the quantity: "))

while quantity <= 0:
    quantity = int(input("Intro the quantity: "))
else:
    for i in range(1,(quantity +1), 2):
        print(f'{i} - {msg}')




