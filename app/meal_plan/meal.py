""""""

from app.mediator import abstract_meal_planner


class Meal(abstract_meal_planner.AbstractMealPlanner):
    def __init__(self, mediator):
        super().__init__()
        self._mediator = mediator
        self.meal = Meal(self._mediator)

    def add_recipe(self, recipe_obj):
        self.recipe_obj = recipe_obj

        

    def update_recipe(self):
        pass
