"""recipe_facade is used to access the classes within the recipe package"""

from app.recipe import recipe
from app.recipe import recipe_box


class RecipeFacade:
    def __init__(self):
        self._recipe = recipe.Recipe
        self._recipe_box = recipe_box.RecipeBox

    def hard_code_new_recipe(self, name, calories, fat, carbs, protein):
        recipe = self._recipe(name, calories, fat, carbs, protein)
        return recipe

    def add_new_recipe(self):
        new_recipe = self._recipe.add_new_recipe()
        return new_recipe

    def create_recipe_box(self, value):
        recipe_box_obj = self._recipe_box.create_recipe_box(value)
        return recipe_box_obj

    def add_recipe_to_box(self, recipe_box_obj, recipe_obj):
        self._recipe_box.add_recipe_to_box(recipe_box_obj, recipe_obj)
        return recipe_box_obj
