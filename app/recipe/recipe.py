"""recipe module for Recipe class"""


class Recipe():

    def __init__(self, recipe_name, calories, fat, carbs, protein):
        self.recipe_name = recipe_name
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


    def add_new_recipe(self):
        print('Please enter a response for each prompt. ')
        recipe_name = input('Enter recipe name: ')
        print('Nutritional info per 1 serving: ')
        calories = input('    Calories: ')
        fat = input('    Fat: ')
        carbs = input('    Carbohydrates: ')
        protein = input('    Protein: ')

        return Recipe(recipe_name, calories, fat, protein, carbs)
