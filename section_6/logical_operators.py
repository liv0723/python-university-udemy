#Logical Operators

#Operator and
print()
print('************ System of discount ***********')
QUANTITY_ARTICLES = 10
quantity_Article_bought = input("Intro the quantity of article to by: ")
is_member = input("Intro is member or not (yes/not): ")

if (int(quantity_Article_bought) >= QUANTITY_ARTICLES) and is_member == 'yes':
    print('has discount')
else:
    print('Don\'t have discount')


#Operator or
print()
print('************ Library *************')
ALLOWED_DISTANCE = 3
user_name = input("Intro yhe name of user: ").lower().strip()
has_credential = input("Intro if has credential (yes/not): ")
live_nearby = input("Intro the km: ")

has_credential = (has_credential == 'yes')
live_nearby = (int(live_nearby) <= ALLOWED_DISTANCE)

if has_credential or live_nearby:
    print(f'The user: {user_name} can be lect books')
else:
    print(f'The user: {user_name} can\'t be lect books')


#Operator not
print('*************** is out of range ********************')
number = int(input("Intro a number: "))
intro_range = not (1 <= number >= 10)

print(f'It\'s in of rage: {intro_range}')
