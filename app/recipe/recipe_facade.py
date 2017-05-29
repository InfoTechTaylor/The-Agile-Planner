"""recipe_facade is used to access the classes within the recipe package"""
from app.recipe import recipe
from app.recipe import recipe_box

class RecipeFacade:
    def __init__(self):
        self._recipe = recipe.Recipe
        self._recipe_box = recipe_box.RecipeBox

    def add_new_recipe(self):
        new_recipe = self._recipe.add_new_recipe()
        return new_recipe

    def get_recipes(self):
        self._recipe_box.get_recipes()