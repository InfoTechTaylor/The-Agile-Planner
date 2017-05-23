"""Command line interface class for displaying output to the user"""

from app.recipe import recipe_box


class UserInterface():
    def __init__(self, mediator):
        self._mediator = mediator

    @staticmethod
    def print_banner():
        print('***************************************************************')
        print('********************* The Agile Planner ***********************')
        print('***************************************************************')
        print()

    @staticmethod
    def print_main_menu():
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

    @staticmethod
    def get_user_choice():
        """
        Get a user's menu option select in form of an int, validate the input, and return
        :return: user_choice
        """
        user_choice = input('Enter the number of the menu option you want to select: ')
        user_choice_valid = False
        user_options = [1, 2, 3, 4, 5]

        while user_choice_valid is False:  # do until user's choice is validated
            user_choice = int(user_choice)
            if user_choice not in user_options:
                user_choice = input('Invalid choice. Option must be a number, 1-3: ')
            else:
                user_choice_valid = True

        return user_choice

    def print_recipe(self, recipe_obj):
        print('-------------------------------------------------------------------'),
        print('| Recipe: ' + recipe_obj.recipe_name),
        print('| Nutritional Info: '),
        print('|   Calories: ' + str(recipe_obj.calories))
        print('|   Fat: ' + str(recipe_obj.fat))
        print('|   Carbs: ' + str(recipe_obj.carbs))
        print('|   Protein: ' + str(recipe_obj.protein))
        print('-------------------------------------------------------------------')

    def start_user_choice(self, user_choice):
        """
        
        :param user_choice: 
        :return: 
        """

        if user_choice == 1:
            self._mediator.recipe.add_new_recipe()
            # recipe.Recipe().add_new_recipe()  --> would have been implemented without mediator design pattern
            self.print_main_menu()
            user_choice = self.get_user_choice()
            self.start_user_choice(user_choice)
        elif user_choice == 2:
            recipe_box.RecipeBox().get_all_recipes()
            self.print_main_menu()
            user_choice = self.get_user_choice()
            self.start_user_choice(user_choice)
        elif user_choice == 3:
            print('\nFEATURE COMING SOON!')
            self.print_main_menu()
            user_choice = self.get_user_choice()
            self.start_user_choice(user_choice)
        elif user_choice == 4:
            recipe_box.RecipeBox().get_all_recipes()
            self._mediator.recipe.update_recipe()
            self.print_main_menu()
            user_choice = self.get_user_choice()
            self.start_user_choice(user_choice)
        elif user_choice == 5:
            exit()


