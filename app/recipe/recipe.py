"""recipe module for Recipe class"""


class Recipe:
    def __init__(self):
        self.recipe_name = None
        self.ingredients_list = []
        self.instructions_list = []
        self.calories = None
        self.fat = None
        self.carbs = None
        self.protein = None

    @staticmethod
    def get_recipe_name():
        print('Please enter a response for each prompt. ')
        recipe_name = input('Enter recipe name: ')
        return recipe_name

    def get_ingredients_list(self):
        print('Enter each ingredient with quantity, pressing enter between each. '
              'When done entering ingredients enter "done":')

        more_ingredients_valid = True
        while more_ingredients_valid is True:
            ingredient = input()
            ingredient_upper = ingredient.upper()
            if ingredient_upper != 'DONE':
                self.ingredients_list.append(ingredient)
            elif ingredient_upper == 'DONE':
                more_ingredients_valid = False
            else:
                pass

        return self.ingredients_list

    def get_instructions_list(self):
        print('Enter each instruction step, pressing enter between each. '
              'When done type "done" then hit enter:')

        more_instructions_valid = True
        while more_instructions_valid is True:
            instruction = input()
            instruction_upper = instruction.upper()
            if instruction_upper != 'DONE':
                self.instructions_list.append(instruction)
            elif instruction_upper == 'DONE':
                more_instructions_valid = False
            else:
                pass

        return self.instructions_list

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

    def static_new_recipe(self, recipe_name, ingredients_list, instructions_list, calories, fat, carbs, protein):
        new_recipe = Recipe()
        new_recipe.recipe_name = recipe_name
        new_recipe.ingredients_list = [ingredients_list]
        new_recipe.instructions_list = [instructions_list]
        new_recipe.calories = calories
        new_recipe.fat = fat
        new_recipe.carbs = carbs
        new_recipe.protein = protein

        return new_recipe

    def add_new_recipe(self):

        self.recipe_name = Recipe.get_recipe_name()
        self.ingredients_list = Recipe.get_ingredients_list(self)
        self.instructions_list = Recipe.get_instructions_list(self)
        self.calories = Recipe.get_recipe_calories()
        self.fat = Recipe.get_recipe_fat()
        self.carbs = Recipe.get_recipe_carbs()
        self.protein = Recipe.get_recipe_protein()

        print()
        print('New recipe created!')

        return Recipe()
