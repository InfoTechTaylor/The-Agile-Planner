""""""

from app.mediator import abstract_meal_planner


class MealPlan(abstract_meal_planner.AbstractMealPlanner):
    def __init__(self, mediator):
        super().__init__(mediator)
        # self._mediator = mediator

    def update_calories(self, recipe_name, updated_calories):
        pass
