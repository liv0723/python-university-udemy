#Oneline Store

print("************ Oneline Store ************")

AMOUNT_BUY = 10000
discount = 0

amount_value = int(input("Intro the amount value of the buys: "))
is_member = input("Intro if is member (yes/not): ")


if amount_value > 1000 and is_member.strip().lower() == 'yes':
    discount = 0.10
elif is_member.strip().lower() == 'yes':
    discount = 0.05


if discount == 0.10:
    discount = amount_value * discount
    final_pay = amount_value - discount
    print(f"""
    amount: ${amount_value}
    discount: ${discount}
    final to pay: ${final_pay}
    """)
elif discount == 0.05:
    discount = amount_value * discount
    final_pay = amount_value - discount
    print(f"""
    amount: ${amount_value}
    discount: ${discount}
    final to pay: ${final_pay}
    """)
else:
    print(f"""
    amount: ${amount_value}
    discount: ${discount}
    final to pay: ${amount_value}
    """)

