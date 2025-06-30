#Break and Continue

print("*********** Break and Continue *************")
total = 0

for i in range(0, 10):
    if i % 2 == 0:
     print(f'is par {i}')

    else:
        print(f'is not par {i}')

    if i != 5:
       print('out of if')
       continue
    else:
        a = 0
        quit()
        #break

print('other')



