# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the singleton, facade, adapter and factory design patterns
along with the iterator design pattern"""

from app.ui import user
from app.recipe import recipe
from app.recipe import recipe_box
from app.ui import adapter
from app.design_patterns import iterator


def main():
    # setup tasks
    # create RecipeBox instance
    recipe_box_obj = recipe_box.RecipeBox.create_recipe_box()

    # create hard coded recipes (in place of a DB implementation)
    recipe1 = recipe.Recipe('hummus', 98, 5.5, 9.9, 3.5)
    recipe2 = recipe.Recipe('banana pancakes', 240, 9.5, 34.8, 6)
    recipe3 = recipe.Recipe('scrambled tofu breakfast burrito', 441, 5, 53.5, 16.5)
    recipe4 = recipe.Recipe('super green smoothie', 225, 9.7, 36.8, 5.8)

    # add recipes to recipe box
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe1)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe2)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe3)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe4)

    # get user's name (in place of a login function to do if planning on having real users)
    user_name = input('Please enter your name to start the program:  ')
    user_obj = user.User(user_name)
    print()

    # print app banner and custom greeting
    adapter_obj = adapter.UIAdapter()
    adapter_obj.display_banner(user_obj.name)

    run_program = True
    while run_program is True:

        user_choice = adapter_obj.display_menu()  # display menu options, get user's choice

        if user_choice == str(1):
            new_recipe = recipe.Recipe.add_new_recipe()
            recipe_box_obj.add_recipe_to_box(recipe_box_obj, new_recipe)
        elif user_choice == str(2):
            # Use Case #1 steps to display each recipe in the recipe box collection
            # iterator design pattern implementation:
            recipe_count = len(recipe_box_obj.recipe_obj_list)
            recipe_box_iterator = iterator.RecipeBoxIterator(recipe_count)
            print()
            while True:
                try:
                    recipe_index = recipe_box_iterator.__next__()
                    recipe_obj = recipe_box_obj.recipe_obj_list[recipe_index]
                    adapter_obj.display_recipe(recipe_obj)
                except StopIteration:
                    break
        elif user_choice == str(3):
            print('Edit recipe feature coming soon!')
            print()
        elif user_choice == str(4):
            pass
        elif user_choice == str(5):
            run_program = False




if __name__ == '__main__':
    main()
