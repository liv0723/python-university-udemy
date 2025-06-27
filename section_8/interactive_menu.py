#Interactive Menu
from enum import nonmember

print("*********** Interactive Menu **************")

option = None

while option != 3:
    option = int(input("""
    Menu:
    1. Create account
    2. Delete Account
    3. Close
    """))
    print( 'Creating account ...' if (option == 1) else 'Delete account ...' if (option == 2) else 'Closing ...' )
else:
    print('Out of Menu')
