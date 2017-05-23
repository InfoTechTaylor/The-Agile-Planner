"""module to hold the MealPlan class that will consist of DailyMealPlan objects"""

from app.mediator import abstract_meal_planner


class MealPlan(abstract_meal_planner.AbstractMealPlanner):
    def __init__(self, mediator):
        super().__init__(mediator)

    def update_calories(self, recipe_obj, updated_calories):
        pass
