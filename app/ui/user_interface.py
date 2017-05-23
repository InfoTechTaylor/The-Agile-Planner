"""Module containing UserInterface class for displaying output to the user"""


class UserInterface():
    def __init__(self, mediator):
        self._mediator = mediator

    @staticmethod
    def print_recipe(recipe_obj):
        print('-------------------------------------------------------------------'),
        print('| Recipe: ' + recipe_obj.recipe_name),
        print('| Nutritional Info: '),
        print('|   Calories: ' + str(recipe_obj.calories))
        print('|   Fat: ' + str(recipe_obj.fat))
        print('|   Carbs: ' + str(recipe_obj.carbs))
        print('|   Protein: ' + str(recipe_obj.protein))
        print('-------------------------------------------------------------------')
