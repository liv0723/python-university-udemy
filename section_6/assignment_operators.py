#Assignment Operator

'''
assignment operator   (=)
'''

name = input("Intro the Name: ")

#assignment multiply
var_1, var_2, var_3 = 1, 2.0, 'pepe'
note_1, note2 = input('first note: '), input("second note: ")
name_1, lastname = input("Intro the name a lastname: ").split(sep= ' ')
value_1, value_2 = ['****', '----']

#assignment string
age_1 = age_2 = input("Intro the same value of age: ")
lade_a = lade_b = lade_c = input("Intro the ;\lade of triangle: ")





#Interchance of value
x, y = 5, 10
x, y = y, x



#Sow the Variables
print ()
print("********* Assignment Operators **********")
print(f"The name is: {name}")
print(f'The vars are using the assignment multiply: ', var_1, var_2, var_3, sep= " ")
print(f'The notes are using the assignment multiply: {note_1}, {note2}')
print(f'The age are using assignment string: {age_1} {age_2} ')
print(f'Lade pf triangle are: Lade A: {lade_a}, Lade B: {lade_b}, Lade C: {lade_c}')
print(f'Tha name is: {name_1}, the lastname is: {lastname}')
print(f'value a: {value_1}, value 2: {value_2}')


