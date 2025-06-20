#inmutability in str

str_1 = "Hello world"
print(str_1)

#str_1[0] = 'h'  can not chance the character
print(str_1)

str_2 = str_1
str_1 = "Bye"
print(str_2)
print(str_1)

if __name__ == "__main__":
    print("ok")
else :
    print("not")