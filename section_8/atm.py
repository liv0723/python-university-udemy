#ATM

print('***************** ATM ***************')

option = 0
balance = 1000.00000
intro_balance = 0.00000

while option != 4:
    option = int(input('''
    Options to make:
    \t1. Check Balance
    \t2. Withdraw Balance
    \t3. Deposit Balance
    \t4. Close
    intro the option: 
    '''))

    if option == 1:
        print(f'Your balance is: {balance:.2f}')
    elif option == 2:
        intro_balance = float(input("Intro the balance to withdraw: "))
        if(intro_balance <= balance and intro_balance >=1):
            balance -= intro_balance
            print(f"Your balance is: {balance:.2f}")
        else:
            print('The value intro is bad')

    elif option == 3:
        intro_balance = float(input("Intro the new balance: "))
        if intro_balance > 1:
            balance += intro_balance
            print(f'Your balance is: {balance:.2f}')
        else:
            print('The value intro is bad')
    elif option == 4:
        print("Closing .......")
    else:
        print("Invalid option ")
else:
    print("Out of ATM")





