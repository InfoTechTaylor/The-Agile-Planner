"""Command line interface class for displaying output to the user"""
from app.recipe import recipe
from app.recipe import recipe_box


class UserInterface:
    def __init__(self):
        pass

    @staticmethod
    def print_banner(self):
        print('***************************************************************')
        print('********************* The Agile Planner ***********************')
        print('***************************************************************')
        print()

    @staticmethod
    def print_menu(self):
        print('Menu Options:')
        print('_____________')
        print('1. Add New Recipe')
        print('2. Browse Recipe Box')
        print('3. Start a meal plan')
        print()

    def get_user_choice(self):
        """
        
        :return: user_choice
        """
        user_choice = input('Enter the number of the menu option you want to select: ')
        user_choice_valid = False
        user_options = [1, 2, 3]

        while user_choice_valid is False:
            user_choice = int(user_choice)
            if user_choice not in user_options:
                user_choice = input('Invalid choice. Option must be a number, 1-3: ')
            else:
                user_choice_valid = True

        if user_choice == 1:
            recipe.Recipe().add_new_recipe()
        elif user_choice == 2:
            recipe_box.RecipeBox().get_all_recipes()


