#Shipping System

print("***************** Shipping System *****************")

destination = input("Intro the destination (national/international): ").strip().lower()
weight = float(input("Intro the weight: "))
cost = None


fee  = 10 if (destination == 'national') else 20
cost = fee * weight

if cost is not None:
    print(f'''
    Destination: {destination}
    weight: {weight}
    cost: {cost}
    ''')

