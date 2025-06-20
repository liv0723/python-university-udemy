employee_name = input("Intro the employee name: ")
employee_age = int(input("Intro the employee age: "))
employee_salary = float(input("Intro the employee salary: "))
is_department_head = input("Intro if a boss (yes/not): ").lower()
while is_department_head != 'yes' and is_department_head != 'not':
    is_department_head = input("Intro if a boss (yes/not): ")


print()
print(f'The employee name are: {employee_name}')
print(f'The employee age are: {employee_age}')
print(f'The employee salary are: {employee_salary}')
if is_department_head == 'yes':
    is_department_head = True
    print(f'The employee is a department head: {is_department_head}')
else:
    is_department_head = False
    print(f'The employee is a department head: {is_department_head}')