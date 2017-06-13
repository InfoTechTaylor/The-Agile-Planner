"""Legacy command line interface class for displaying output to the user, to be accessed by adapter.py"""


class UserInterface():
    def __init__(self):
        pass

    @staticmethod
    def print_welcome_banner():
        print('***************************************************************')
        print('********************* The Agile Planner ***********************')
        print('***************************************************************')
        print()

    def get_user_first_name(self):
        first_name = input('Enter your first name:  ')

        return first_name

    def get_user_last_name(self):
        last_name = input('Enter your last name: ')

        return last_name

    def print_greeting(self, first_name):
        print('Hello, ' + first_name + ', let\'s start planning!')

    def print_nutritional_goals_prompt(self):
        user_choice = input('Do you want to set nutritional goals for your meal planning? (y/n) ')

        return user_choice

    @staticmethod
    def print_recipe(recipe_obj):
        print('-------------------------------------------------------------------'),
        print('| Recipe: ' + recipe_obj.recipe_name),
        print('| Ingredients: ')
        for ingredient in recipe_obj.ingredients_list:
            print('|     ' + ingredient)
        print('| Instructions: ')
        for instruction in recipe_obj.instructions_list:
            print('|     ' + instruction)
        print('| Nutritional Info: '),
        print('|   Calories: ' + str(recipe_obj.calories))
        print('|   Fat: ' + str(recipe_obj.fat))
        print('|   Carbs: ' + str(recipe_obj.carbs))
        print('|   Protein: ' + str(recipe_obj.protein))
        print('-------------------------------------------------------------------')
