# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the singleton, facade, adapter and factory design patterns"""

from app.ui import user
from app.recipe import recipe_facade
from app.ui import adapter
from app.meal_plan import meal_factory


def main():

    #  1. Singleton implementation: assert only one instance of User is created due to Singleton pattern on User
    #  See app.ui.user for class implementation of Singleton
    user_name = input('Please enter your name to start the program:  ')
    user_obj = user.User(user_name)
    user_obj = user.User('Joe Somebody')  # Singleton won't allow this, user name printed will not be 'Joe Somebody'
    print()

    # 2. Adapter implementation: access the UserInterface class through an adapter to display the app welcome banner
    adapter_obj = adapter.UIAdapter()
    adapter_obj.display_banner(user_obj.name)  # note the user's name in banner is the one you entered

    # 3. Facade implementation: access the add_new_recipe() method of Recipe, and create_recipe_box()/
    # add_new_recipe_to_box() of RecipeBox through the recipe facade
    recipe_facade_obj = recipe_facade.RecipeFacade()  # create facade object to access recipe module
    recipe_box_obj = recipe_facade_obj.create_recipe_box()  # create recipe box to add recipes to
    new_recipe_obj = recipe_facade_obj.add_new_recipe()  # create new recipe obj
    recipe_facade_obj.add_recipe_to_box(recipe_box_obj, new_recipe_obj)  # add new recipe to recipe box
    adapter_obj.display_recipe(new_recipe_obj)  # demonstrates use of UI adapter again

    # 4. Factory implementation
    # using a recipe object added in step #2 above, ask user what meal they'd like to add it to
    # and create the appropriate meal time object to add that recipe to
    meal_choice = input('What meal would you like to add your new recipe to? (breakfast, lunch, or dinner):  ')
    meal_factory_obj = meal_factory.MealFactory()
    meal = meal_factory_obj.create_meal(meal_choice)
    meal.add_recipe(meal, new_recipe_obj)


if __name__ == '__main__':
    main()
