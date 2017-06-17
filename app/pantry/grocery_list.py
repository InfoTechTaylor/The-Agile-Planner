'''grocery list module'''
from app.design_patterns import singleton


class GroceryList(metaclass=singleton.Singleton):
    def __init__(self):
        self.grocery_list = []

    def add_item_to_list(self, item):
        self.grocery_list.append(item)

    def add_recipe_ingredients(self, recipe_obj):
        for ingredient in recipe_obj.list:
            self.add_item_to_list(ingredient)
