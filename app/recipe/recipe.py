"""recipe module for Recipe class"""

from app.mediator import abstract_meal_planner


class Recipe(abstract_meal_planner.AbstractMealPlanner):

    def __init__(self, mediator):
        super().__init__()
        self._mediator = mediator

    def add_ingredients_list(self):
        ingredients_list = []
        ingredient = input('Enter each ingredient with quantity, pressing enter between each. '
                           'When done entering ingredients enter "done": \n')
        ingredients_list.append(ingredient)

        more_ingredients_valid = True
        while more_ingredients_valid is True:
            ingredient = input()
            ingredient_upper = ingredient.upper()

            if ingredient_upper != 'DONE':
                ingredients_list.append(ingredient)
            elif ingredient_upper == 'DONE':
                more_ingredients_valid = False
            else:
                pass

        return ingredients_list

    def add_new_recipe(self):
        print('Please enter a response for each prompt. ')
        recipe_name = input('Enter recipe name: ')
        # ingredients_list = self.add_ingredients_list()
        # TODO add instructions_list = self.add_instructions_list()
        # prep_time = input('Enter prep time in minutes: ')
        # cook_time = input('Enter cook time in minutes: ')
        # serving_size = input('Enter serving size: ')
        # recipe_source = input('Enter the name of cookbook or blog for recipe: ')
        # recipe_url = input('If applicable, enter URL of source. If not, hit Enter: ')
        print('Nutritional info per 1 serving: ')
        calories = input('    Calories: ')
        fat = input('    Fat: ')
        # saturated_fat = input('    Saturated Fat: ')
        carbs = input('    Carbohydrates: ')
        # sugar = input('    Sugar: ')
        protein = input('    Protein: ')
        # sodium = input('    Sodium: ')
        # fiber = input('    Fiber: ')

        # new_recipe_list = [recipe_name, '', '', prep_time, cook_time, serving_size, recipe_source, recipe_url,
        #                   calories, fat, saturated_fat, carbs, sugar, protein, sodium, fiber]
        # TODO add additional recipe attributes (ingredients and instructions take special care with adding to csv)
        new_recipe_list = (recipe_name, calories, fat, protein, carbs)

        recipe_box_csv = open('recipe/recipe_box.csv', 'a')
        new_recipe_string = ""
        for item in new_recipe_list:
            # item = str(item)
            new_recipe_string += item + ','
        recipe_box_csv.write(new_recipe_string)
        recipe_box_csv.write('\n')
        recipe_box_csv.close()

    def update_recipe(self):
        recipe_name = input('Enter the name of the recipe you want to edit: ')

        recipe_box_csv = open('recipe/recipe_box.csv', 'r')
        for row in recipe_box_csv:
            if row[0] == recipe_name:
                print('recipe found!')

