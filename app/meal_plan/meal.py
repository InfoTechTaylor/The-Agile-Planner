"""Meal classes"""
from abc import ABC, abstractmethod


class AbstractMeal(ABC):
    def __init__(self):
        self.recipe_list = []
        self.total_calories = 0

    @abstractmethod
    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj

    def update(self):
        pass


class Breakfast(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Breakfast'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)

        print()
        print('New recipe added to your breakfast!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

        return meal_obj

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories


class Lunch(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Lunch'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)

        print()
        print('New recipe added to your breakfast!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

        return meal_obj

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories


class Dinner(AbstractMeal):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Dinner'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)

        print()
        print('New recipe added to your breakfast!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

        return meal_obj

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories
