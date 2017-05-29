"""Meal classes"""
from abc import ABC, abstractmethod


class AbstractMeal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj


class Breakfast(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Breakfast'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj
        print()
        print('New recipe added to your breakfast!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + recipe_obj.calories)


class Lunch(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Lunch'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj
        print()
        print('New recipe added to your lunch!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + recipe_obj.calories)


class Dinner(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Dinner'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj
        print()
        print('New recipe added to your dinner!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + recipe_obj.calories)
