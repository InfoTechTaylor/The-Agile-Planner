"""recipe_box module for RecipeBox class. Ensure that RecipeBox only has one instance by importing singleton.
Implement singleton.Singleton as metaclass for RecipeBox"""

from app.design_patterns import singleton


class RecipeBox(metaclass=singleton.Singleton):  # RecipeBox is an instance of Singleton due to use of metaclass
    def __init__(self):
        self.recipe_obj_list = []
        self.value = len(self.recipe_obj_list)

    @classmethod
    def create_recipe_box(cls):
        return cls()

    @staticmethod
    def add_recipe_to_box(recipe_box_obj, recipe_obj):
        recipe_box_obj.recipe_obj_list.append(recipe_obj)
        return recipe_box_obj

    def select_recipe(self):
        for recipe in self.recipe_obj_list:
            print('Recipe name: ' + recipe.recipe_name)
            print('Calories: ' + str(recipe.calories))
            print('Carbs: ' + str(recipe.carbs))
            print('Fat: ' + str(recipe.fat))
            print('Protein: ' + str(recipe.protein))

            selection = input('Press x if you want to add this recipe to your meal, otherwise hit enter: ')
            print()

            if selection == 'x':
                selected_recipe = recipe
                break
            else:
                pass

        return selected_recipe
