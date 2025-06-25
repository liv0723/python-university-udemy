#Mirror of house

print("*********** house of house *************")

MAYOR  = 10

age = int(input("Intro the age: "))
fear = input("you have fear to the dark (yes/not): ") == 'yes'

if age > 10 and not fear:
    print("you can intro")
else:
    print('you do not intro')

