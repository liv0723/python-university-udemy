#Cumulative Sum

print("************* Cumulative Sum *****************")

MAXIMUM = 5
iterator = 0
while_sum = 0
for_sum = 0

while iterator <= MAXIMUM:
    while_sum += iterator
    print(while_sum, end=' ' )
    iterator += 1

print(f"\nThe cumulative sum using while is: {while_sum}")

for ite in range(MAXIMUM):
    for_sum += ite
    print(for_sum, end= ' ')

print(f"\nThe cumulative sum using for is: {for_sum}")


