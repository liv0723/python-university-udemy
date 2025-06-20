print("****** Cooking Recipe ******")
cooking_recipe_name = input('Intro the name of Cooking Recipe: ')
ingredients = input('Intro the Ingredients:  ')
preparation_time = int(input("Intro the preparation time in minute mayor to 0: "))
while preparation_time <= 0:
    preparation_time = int(input("Intro the preparation time: "))
difficulty = input("Intro the Difficulty (easy, medium, high ): ").lower()
while difficulty != 'easy' and difficulty != 'medium' and difficulty != 'high':
    difficulty = input("Intro the Difficulty (easy, medium, high ): ").lower()


print()
print('******** Cooking Recipe *********')
print(f'The name of Cooking Recipe are: {cooking_recipe_name}')
print(f'Ingredients of Cooking Recipe: {ingredients}')
print(f'quantity of ingredients: {len(ingredients.split(sep= ' '))} ')
print(f'Preparation time of Cooking Recipe: {preparation_time}')
print(f'Difficulty of Cooking Recipe: {difficulty}')


