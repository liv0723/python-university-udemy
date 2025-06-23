print("************ sales ticket **************")

count = 0
total = 0
data = []
discount = 0.10
subtotal = 0

while count < 2:
    product = input("Intro the product and de price, separated by ( ): ").strip()
    data.append(product)
    name,price = data[count].split()
    total += int(price)
    count += 1

tax = total * 0.16

if total > 7:
    subtotal = total *discount


for aux in data:
    print(aux)
print(f"""
Subtotal: $ {total} 
Tax: $ {tax}
Discount: $ {discount}
Total: {subtotal}""")







