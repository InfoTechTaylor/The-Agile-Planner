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
from app.meal_plan import meal_factory
from app.design_patterns import command


def main():
    ######################################################################################
    # SETUP TASKS
    ######################################################################################
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

    # print app banner and custom greeting
    adapter_obj = adapter.UIAdapter()
    adapter_obj.display_banner()

    ######################################################################################
    # ITERATOR DESIGN PATTERN IMPLEMENTATION
    ######################################################################################
    # iterate through recipes in recipe box to display all recipes

    recipe_count = len(recipe_box_obj.recipe_obj_list)
    recipe_box_iterator = iterator.RecipeBoxIterator(recipe_count)
    print()
    print('Here is the contents of your recipe box: ')
    while True:
        try:
            recipe_index = recipe_box_iterator.__next__()
            recipe_obj = recipe_box_obj.recipe_obj_list[recipe_index]
            adapter_obj.display_recipe(recipe_obj)
        except StopIteration:
            break

    ######################################################################################
    # COMMAND DESIGN PATTERN IMPLEMENTATION
    ######################################################################################
    # create meal object: meal_obj is receiver, add_recipe is the command action
    meal_factory_obj = meal_factory.MealFactory()
    meal_obj_receiver = meal_factory_obj.create_meal('breakfast')

    # create add recipe command to send to the invoker to hold until execution
    add_recipe3_command = command.AddRecipeToMealCommand(meal_obj_receiver, recipe3)
    add_recipe4_command = command.AddRecipeToMealCommand(meal_obj_receiver, recipe4)
    add_recipe1_command = command.AddRecipeToMealCommand(meal_obj_receiver, recipe1)

    # add commands to invoker list
    command_invoker = command.Invoker()
    command_invoker.add_command(add_recipe3_command)
    command_invoker.add_command(add_recipe4_command)
    command_invoker.add_command(add_recipe1_command)

    # undo adding recipe1 to the meal
    command_invoker.undo_command(add_recipe1_command)

    # execute the command list that invoker holds
    command_invoker.execute_commands()

if __name__ == '__main__':
    main()
