"""recipe module for Recipe class"""


class Recipe(object):

    def __init__(self, recipe_name, calories, fat, carbs, protein):
        self.recipe_name = recipe_name
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


    @classmethod
    def add_new_recipe(cls):
        print('Please enter a response for each prompt. ')
        recipe_name = input('Enter recipe name: ')
        print('Nutritional info per 1 serving: ')
        calories = input('    Calories: ')
        fat = input('    Fat: ')
        carbs = input('    Carbohydrates: ')
        protein = input('    Protein: ')

        new_recipe = cls(recipe_name, calories, fat, protein, carbs)

        print()
        print('New recipe created:')

        return new_recipe
