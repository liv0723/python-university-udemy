#Health and fitness

print("********** Health and Fitness **********")

DAILY_STEPS_GOAL = 10000
CALORIES_DAILY_STEPS = 0.04

user_name = input("Intro the name of user: ")
daily_steps = int(input("Intro the steps daily: "))

burn_calories = daily_steps * CALORIES_DAILY_STEPS

it_was_fulfilled = "was fulfilled" if daily_steps > DAILY_STEPS_GOAL else 'do not fulfilled '

print(f' The user: {user_name}\n',it_was_fulfilled, f'\n and the steps are: {daily_steps}\n',f'and calorie: {burn_calories}', sep= ' ')
