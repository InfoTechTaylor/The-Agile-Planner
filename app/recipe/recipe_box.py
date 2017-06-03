"""recipe_box module for RecipeBox class. Ensure that RecipeBox only has one instance by importing singleton.
Implement singleton.Singleton as metaclass for RecipeBox"""

from app.design_patterns import singleton
from app.design_patterns import iterator


class RecipeBox(metaclass=singleton.Singleton):  # RecipeBox is an instance of Singleton due to use of metaclass
    def __init__(self, value):
        self.recipe_obj_list = []
        self.value = value

    def __iter__(self):
        return iterator.RecipeBoxIterator(self.value)

    @classmethod
    def create_recipe_box(cls, value):
        return cls()

    @staticmethod
    def add_recipe_to_box(recipe_box_obj, recipe_obj):
        recipe_box_obj.recipe_obj_list.append(recipe_obj)
        return recipe_box_obj
