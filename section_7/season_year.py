#Season of Year

print("************* Season of Year ************")

month_year = int(input("Intro the month of the year: "))
season = ""

while month_year < 1 or month_year >12:
    month_year = int(input("Intro the month of the year: "))

if month_year == 1 or month_year == 2 or month_year == 12:
    season = 'Winter'
elif month_year == 3 or month_year == 4 or month_year == 5:
    season = 'Spring'
elif month_year == 6 or month_year == 7 or month_year == 8:
    season = 'Summer'
else:
    season = 'Autumn'

print(f'The season is: {season}')


