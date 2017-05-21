""""""

from app.mediator import abstract_meal_planner


class DailyMealPlan(abstract_meal_planner.AbstractMealPlanner):
    def __init__(self, mediator):
        super().__init__()
        self._mediator = mediator

    def update_recipe(self):
        pass