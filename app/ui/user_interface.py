"""Command line interface class for displaying output to the user"""

from app.recipe import recipe_box


class UserInterface():
    def __init__(self):
        pass

    @staticmethod
    def print_welcome_banner():
        print('***************************************************************')
        print('********************* The Agile Planner ***********************')
        print('***************************************************************')
        print()
        print("Let's start meal planning!")
        print("First, you'll enter a recipe you'd like to add to your meal plan.")
        print()

    def print_recipe(self, recipe_obj):
        print('-------------------------------------------------------------------'),
        print('| Recipe: ' + recipe_obj.recipe_name),
        print('| Nutritional Info: '),
        print('|   Calories: ' + str(recipe_obj.calories))
        print('|   Fat: ' + str(recipe_obj.fat))
        print('|   Carbs: ' + str(recipe_obj.carbs))
        print('|   Protein: ' + str(recipe_obj.protein))
        print('-------------------------------------------------------------------')
