#Grading System
from enum import nonmember

from section_7.health_fitness import it_was_fulfilled

print("*************** Grading System **************")

grading = int(input("Intro the grading between 1-10:"))

while grading < 1 or grading > 10:
    grading = int(input("Intro the grading between 1-10:"))

grading = 'A' if (grading == 9 or grading == 10) else 'B' if (grading == 8 or grading == 7) else 'C' if (grading == 6 or grading == 5) else 'D' if (grading == 4 or grading == 3) else 'F'

print(f'The grading is {grading}')




