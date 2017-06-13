# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the singleton, facade, adapter and factory design patterns
along with the iterator design pattern"""

from app.recipe import recipe, recipe_box
from app.ui import user_interface, user
from app.meal_plan import meal, meal_plan


def main():
    ##########################
    # SETUP
    ##########################
    # create RecipeBox instance
    recipe_box_obj = recipe_box.RecipeBox.create_recipe_box()

    # create hard coded recipes (in place of a DB implementation)
    recipe1 = recipe.Recipe.static_new_recipe(recipe.Recipe(), 'Salad', 'lettuce, dressing, cucumber',
                                              '1. Step one, 2. step 2',
                                              300, 23, 4, 2)
    recipe2 = recipe.Recipe.static_new_recipe(recipe.Recipe(), 'Pasta', 'dry pasta, sauce',
                                              '1. Step one, 2. step 2',
                                              300, 23, 4, 2)
    recipe3 = recipe.Recipe.static_new_recipe(recipe.Recipe(), 'Burger', 'burger patties, bread buns',
                                              '1. Step one, 2. step 2',
                                              300, 23, 4, 2)

    # add recipes to recipe box
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe1)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe2)
    recipe_box_obj.add_recipe_to_box(recipe_box_obj, recipe3)

    ########################################################################
    # USE CASE 3: New User, New Goals
    ########################################################################
    # Known issue: no input validation or validation that macronutrients add up to 100%
    ui_obj = user_interface.UserInterface()
    ui_obj.print_welcome_banner()
    first_name = ui_obj.get_user_first_name()  # 1. , 2.
    last_name = ui_obj.get_user_last_name()
    user_obj = user.User(first_name, last_name)
    ui_obj.print_greeting(first_name)
    set_nutritional_goals = ui_obj.print_nutritional_goals_prompt()  # 3. , 4.

    # Get the nutritional goals from user and set them in user settings/attributes
    if set_nutritional_goals == 'y':
        calories = input('What is your daily calorie goal? ')
        user_obj.set_daily_calorie_goal(calories)
        carbs = input('What percentage of 100 is your carbs goal? (enter 60 if unsure) ')
        user_obj.set_daily_carb_goal(carbs)
        fat = input('What percentage of 100 is your fat goal? (enter 20 if unsure) ')
        user_obj.set_daily_fat_goal(fat)
        protein = input('What percentage of 100 is your protein goal? (enter 20 if unsure) ')
        user_obj.set_daily_protein_goal(protein)

    # summarize goals to the user
    print()
    print('Your goals have been saved: ')
    print('Daily calorie goal: ' + user_obj.daily_calorie_goal)
    print('Daily carb goal: ' + user_obj.daily_carb_goal + '%')
    print('Daily fat goal: ' + user_obj.daily_fat_goal + '%')
    print('Daily protein goal: ' + user_obj.daily_protein_goal + '%')

    ########################################################################
    # USE CASE #1 Add New Recipe
    ########################################################################
    print()
    print('Let\'s start by adding a new recipe.')
    recipe_obj = recipe.Recipe()
    recipe_obj.add_new_recipe()

    ui_obj.print_recipe(recipe_obj)

    ########################################################################
    # USE CASE #2 Meal Planning
    ########################################################################
    # 1. browse and select a recipe
    print()
    print('Let\'s add a recipe to your meal plan!')
    selected_recipe = recipe_box_obj.select_recipe()

    # 2. add recipe to meal
    meal_obj = meal.Lunch()
    meal_obj.add_recipe(meal_obj, selected_recipe)
    meal_obj.calculate_calories()

    # 3. add meal to daily meal plan
    day_meal_plan = meal_plan.DailyMealPlan('Sunday')
    day_meal_plan = meal_plan.DailyMealPlan.add_meal(day_meal_plan, meal_obj)
    day_meal_plan.calculate_calories()

    # 4. add day meal plan to week meal plan
    week_meal_plan = meal_plan.MealPlan('6/26/17')
    week_meal_plan = week_meal_plan.add_daily_meal_plan(day_meal_plan)
    week_meal_plan.calculate_calories()

    # 5. display meal plan
    print()
    print('#######################################################################################')
    print('Displaying your meal plan for the week of ' + week_meal_plan.start_date + ':')
    print('Day: ' + day_meal_plan.day_of_week)
    print('Meal: ' + meal_obj.meal_type)
    print('Recipe(s): ' + selected_recipe.recipe_name)
    print('#######################################################################################')

if __name__ == '__main__':
    main()
