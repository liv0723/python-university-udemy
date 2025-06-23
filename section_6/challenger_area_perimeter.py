#Challenger Area and Perimeter

print("*************** Area and Perimeter **************")
lade_a,lade_b = input("Intro the lade of rectangle separated by ' ': ").strip().split()
area = 0
perimeter = 0

lade_a_normalize = int(lade_a)
lade_b_normalize = int(lade_b)

if lade_a and lade_b:
    area = lade_a_normalize * lade_b_normalize
    perimeter = 2*(lade_a_normalize + lade_b_normalize)

print(f'The area is: {area}')
print(f'The perimeter is: {perimeter}')