"""recipe module for Recipe class"""


class Recipe:
    def __init__(self, recipe_name, calories, fat, carbs, protein):
        self.recipe_name = recipe_name
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    @staticmethod
    def get_recipe_name():
        print('Please enter a response for each prompt. ')
        recipe_name = input('Enter recipe name: ')
        return recipe_name

    @staticmethod
    def get_recipe_calories():
        print('Nutritional info per 1 serving: ')
        calories = input('    Calories: ')
        return calories

    @staticmethod
    def get_recipe_fat():
        fat = input('    Fat: ')
        return fat

    @staticmethod
    def get_recipe_carbs():
        carbs = input('    Carbohydrates: ')
        return carbs

    @staticmethod
    def get_recipe_protein():
        protein = input('    Protein: ')
        return protein

    def add_new_recipe(self):

        recipe_name = Recipe.get_recipe_name()
        calories = Recipe.get_recipe_calories()
        fat = Recipe.get_recipe_fat()
        carbs = Recipe.get_recipe_carbs()
        protein = Recipe.get_recipe_protein()

        new_recipe = Recipe(recipe_name, calories, fat, protein, carbs)

        print()
        print('New recipe created!')

        return new_recipe