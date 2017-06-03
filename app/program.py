# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the singleton, facade, adapter and factory design patterns
along with the iterator design pattern"""

from app.ui import user
from app.recipe import recipe_facade
from app.ui import adapter
from app.design_patterns import iterator



def main():

    # get user's name (in place of a login function to do if planning on having real users)
    user_name = input('Please enter your name to start the program:  ')
    user_obj = user.User(user_name)
    print()

    # print app banner and custom greeting
    adapter_obj = adapter.UIAdapter()
    adapter_obj.display_banner(user_obj.name)

    # Use Case #1 Precondition: Make RecipeBox instance
    recipe_facade_obj = recipe_facade.RecipeFacade()  # create facade object to access recipe module
    recipe_box_obj = recipe_facade_obj.create_recipe_box(0)  # create recipe box to add recipes to

    # Use Case #1 Precondition: populate RecipeBox instance with hard coded recipes (in place of DB implementation)
    recipe1 = recipe_facade_obj.hard_code_new_recipe('hummus', 98, 5.5, 9.9, 3.5)
    recipe2 = recipe_facade_obj.hard_code_new_recipe('banana pancakes', 240, 9.5, 34.8, 6)
    recipe3 = recipe_facade_obj.hard_code_new_recipe('scrambled tofu breakfast burrito', 441, 5, 53.5, 16.5)
    recipe4 = recipe_facade_obj.hard_code_new_recipe('super green smoothie', 225, 9.7, 36.8, 5.8)

    # TODO update add recipe to box function to take a list to reduce lines of code
    recipe_facade_obj.add_recipe_to_box(recipe_box_obj, recipe1)
    recipe_facade_obj.add_recipe_to_box(recipe_box_obj, recipe2)
    recipe_facade_obj.add_recipe_to_box(recipe_box_obj, recipe3)
    recipe_facade_obj.add_recipe_to_box(recipe_box_obj, recipe4)

    # Use Case #1 steps to display each recipe in the recipe box collection
    recipe_box_iterator = iterator.RecipeBoxIterator(4)

    while True:
        try:
            recipe = recipe_box_iterator.__next__()
            adapter_obj.display_recipe(recipe)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
