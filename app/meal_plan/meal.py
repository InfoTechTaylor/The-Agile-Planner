"""Meal classes"""


class Meal:
    def __init__(self, meal_type):
        super().__init__()
        self.meal_type = meal_type
        self.list = []  # list of Recipe() objects
        self.total_calories = 0

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.list.append(recipe_obj)

        return meal_obj
