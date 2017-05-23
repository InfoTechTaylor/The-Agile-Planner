# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This version of the app is implementing the Mediator design pattern
This app was written using Python version 3.5.2"""

from app.mediator import mediator_classes


def main():
    # to demonstrate mediator design implementation
    mediator_obj = mediator_classes.Mediator()
    recipe_obj = mediator_obj.recipe
    meal_obj = mediator_obj.meal
    ui = mediator_obj.ui

    # print recipe and meal prior to changes
    ui.print_recipe(recipe_obj)  # UI & Recipe interaction through Mediator
    # display meal information that contains the recipe object
    print()
    print('MEAL OVERVIEW:')
    print(meal_obj.meal_type)
    print(meal_obj.recipe.recipe_name)
    print('Calories for Meal: ' + str(meal_obj.recipe.calories))
    print()

    # execute update_calories() method of Recipe
    recipe_obj.update_calories(recipe_obj, 250)

    # print recipe and meal after changes
    ui.print_recipe(recipe_obj)  # UI & Recipe interaction through Mediator
    # display meal information that contains the recipe object
    print()
    print('MEAL OVERVIEW:')
    print(meal_obj.meal_type)
    print(meal_obj.recipe.recipe_name)
    print('Calories for Meal: ' + str(meal_obj.recipe.calories))
    print()


if __name__ == '__main__':
    main()
