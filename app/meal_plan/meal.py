"""meal module for the Meal class which inherits from AbstractMealPlanner"""

from app.mediator import abstract_meal_planner


class Meal(abstract_meal_planner.AbstractMealPlanner):
    def __init__(self, mediator, meal_type, recipe):
        super().__init__(mediator)
        self.meal_type = meal_type
        self.recipe = recipe

    def add_recipe(self, recipe_obj):
        pass

    def update_calories(self, recipe_obj, updated_calories):
        print('Calories in ' + str(recipe_obj.recipe_name) + ' updated to ' + str(updated_calories) + ' calories!')
