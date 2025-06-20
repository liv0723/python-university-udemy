#SubSTR

message = "This is a message is"

print(message[0:4])
print(message[:3])
print(message[5:])
print(message.find("is"))
print(message.find("is",4,10))
print(message.replace("This", 'THIS'))
print(message.endswith('e'))
print(message.split())
print(message.replace("is", 'IS', 2))
print( "this-is-separated-by".rsplit('-') )
aux = message.split()
print("".join(aux[1:3]))


