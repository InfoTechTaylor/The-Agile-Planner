"""recipe_facade is used to access the classes within the recipe package"""
from app.recipe import recipe
from app.recipe import recipe_box

class RecipeFacade:
    def __init__(self):
        self._recipe = recipe.Recipe('Pizza', 300, 5, 30, 6)
        self._recipe_box = recipe_box.RecipeBox

    def access_recipe_methods(self):
        self._recipe.add_new_recipe()

    def access_recipe_box_methods(self):
        self._recipe_box.get_recipes()