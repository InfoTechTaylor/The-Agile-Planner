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
    user1 = user.User('Taylor')
    user2 = user.User('Brett')
    assert user1 is user2
    print('No AssertionError thrown, second user never created as both user variables are set to Taylor: ')
    print('User1 variable name: ' + str(user1.name))
    print('User2 variable name: ' + str(user2.name))
    print()

    # 2. Adapter implementation: access the UserInterface class through an adapter to display the app welcome banner
    adapter_obj = adapter.UIAdapter()
    adapter_obj.display_banner()

    # 3. Facade implementation: access the add_new_recipe() method of Recipe through the recipe facade
    recipe_facade_obj = recipe_facade.RecipeFacade()  # create facade object to access recipe module
    new_recipe_obj = recipe_facade_obj.add_new_recipe()
    adapter_obj.display_recipe(new_recipe_obj)  # demonstrates use of UI adapter again

    # 4. Factory implementation
    # using a recipe object added in step #2 above, ask user what meal they'd like to add it to
    # and create the appropriate meal time object to add that recipe to
    meal_choice = input('What meal would you like to add your new recipe to? (breakfast, lunch, or dinner:  ')
    meal_factory_obj = meal_factory.MealFactory()
    meal = meal_factory_obj.create_meal(meal_choice)
    meal.add_recipe(meal, new_recipe_obj)


if __name__ == '__main__':
    main()
