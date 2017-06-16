"""Meal classes"""
from abc import ABC, abstractmethod


class AbstractMeal(ABC):
    def __init__(self):
        self.recipe_list = []
        self.total_calories = 0

    @abstractmethod
    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)

        return meal_obj

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories


class Meal(AbstractMeal):
    def __init__(self, meal_type):
        super().__init__()
        self.meal_type = meal_type

    def add_recipe(self, meal_obj, recipe_obj):
        pass

    def calculate_calories(self):
        pass
