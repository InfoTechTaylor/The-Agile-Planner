# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the singleton, facade, adapter and factory design patterns
along with the iterator design pattern"""

from app.recipe import recipe, recipe_box
from app.ui import adapter
from app.meal_plan import meal_factory, meal_plan
from app.design_patterns import command, iterator


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
    recipe5 = recipe.Recipe('thai salad with peanut tempeh', 441, 23.7, 43.3, 21.1)
    recipe6 = recipe.Recipe('marinated peanut tempeh', 250, 15.2, 19.3, 13.4)

    # add recipes to recipe box
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe1)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe2)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe3)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe4)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe5)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe6)

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
    # CHAIN OF RESPONSIBILITY DESIGN PATTERN IMPLEMENTATION
    ######################################################################################
    # setup, add a meal with recipes & create handlers for each item in the chain
    meal_factory_obj = meal_factory.MealFactory()
    meal_plan_handler = meal_plan.MealPlan(None)
    daily_meal_handler = meal_plan.DailyMealPlan(meal_plan_handler)
    meal_handler = meal_factory_obj.create_meal('lunch', daily_meal_handler)  # meal object starts the chain with no successor

    # add recipes to starting meal
    meal_handler.add_recipe(meal_handler, recipe5)
    meal_handler.add_recipe(meal_handler, recipe6)

    # add meal to a day's meal plan, then add that day meal plan to the overall meal plan
    daily_meal_handler.add_meal(meal_handler)
    meal_plan_handler.add_daily_meal_plan(daily_meal_handler)

    # execute the handle_request method throughout the chain which calculates total calories
    meal_handler.handle_request()  # calculates total calories for meal, daily meal plan, and meal plan

    print()
    print('Total Calories Summary:')
    print('Total Calories for ' + meal_handler.meal_type + ' : ' + str(meal_handler.total_calories))
    print('Total Calories for the day : ' + str(daily_meal_handler.total_calories))
    print('Total Calories for the week : ' + str(meal_plan_handler.total_calories))

    ######################################################################################
    # COMMAND DESIGN PATTERN IMPLEMENTATION
    ######################################################################################
    # create meal object: meal_obj is receiver, add_recipe is the command action
    meal_obj_receiver = meal_factory_obj.create_meal('breakfast', None)

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
