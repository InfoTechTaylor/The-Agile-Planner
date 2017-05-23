"""recipe module for Recipe class"""

from app.mediator import abstract_meal_planner


class Recipe(abstract_meal_planner.AbstractMealPlanner):

    def __init__(self, mediator, recipe_name, calories, fat, carbs, protein):
        super().__init__(mediator)
        # self._mediator = mediator
        self.recipe_name = recipe_name
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def update_calories(self, recipe_obj, updated_calories):

        recipe_obj.calories = updated_calories
        self._mediator.notify_update_calories(recipe_obj, updated_calories)
