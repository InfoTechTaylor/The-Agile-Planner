"""Legacy command line interface class for displaying output to the user, to be accessed by adapter.py"""


class UserInterface():
    def __init__(self):
        pass

    @staticmethod
    def print_welcome_banner(user_name):
        print('***************************************************************')
        print('********************* The Agile Planner ***********************')
        print('***************************************************************')
        print()
        print("Hello, " + user_name + "! Let's start meal planning!")

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

    def print_menu(self):

        print()
        print('________________________________________________________________')
        print('Menu Options:')
        print('________________________________________________________________')
        print('1. Add New Recipe')
        print('2. Browse Recipe Box')
        print('3. Start a meal plan')
        print('4. Edit Recipe')
        print('5. Exit program')
        print()

        user_choice = input('Please enter a number choice from the menu: ')

        return user_choice
