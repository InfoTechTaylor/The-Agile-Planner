"""Meal classes"""
from abc import ABC, abstractmethod
from app.design_patterns import chain_of_responsibility


class AbstractMeal(ABC):
    def __init__(self):
        self.recipe_list = []
        self.total_calories = 0

    @abstractmethod
    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe = recipe_obj

    def update(self):
        pass


class Breakfast(AbstractMeal, chain_of_responsibility.AbstractHandler):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Breakfast'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)
        print()
        print('New recipe added to your breakfast!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories

    def handle_request(self):
        self.calculate_calories()
        self.successor.handle_request()


class Lunch(AbstractMeal, chain_of_responsibility.AbstractHandler):
    def __init__(self, successor):
        super().__init__()
        self.meal_type = 'Lunch'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)
        print()
        print('New recipe added to your lunch!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories

    def handle_request(self):
        if True:
            pass
        elif self.successor is not None:
            self.successor.handle_request()


class Dinner(AbstractMeal, chain_of_responsibility.AbstractHandler):
    def __init__(self):
        super().__init__()
        self.meal_type = 'Dinner'

    def add_recipe(self, meal_obj, recipe_obj):
        meal_obj.recipe_list.append(recipe_obj)
        print()
        print('New recipe added to your dinner!')
        print('Recipe Name: ' + recipe_obj.recipe_name)
        print('Total Calories: ' + str(recipe_obj.calories))

    def calculate_calories(self):
        for recipe in self.recipe_list:
            self.total_calories += recipe.calories

        return self.total_calories

    def handle_request(self):
        if True:
            self.calculate_calories()
        elif self.successor is not None:
            self.successor.handle_request()
