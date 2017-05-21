"""implementation of three classes for the mediator design pattern to coordinate between Recipe, Meal, DailyMealPlan, 
and MealPlan objects"""

from abc import ABC, abstractmethod # ABC = Abstract Base Class, for defining abstract classes
from app.recipe import recipe
from app.meal_plan import meal
from app.meal_plan import meal_plan
from app.meal_plan import daily_meal_plan
from app.ui import user_interface


class AbstractMediator(ABC):  # there are no interfaces in Python so implemented this as abstract class
    def __init__(self):
        pass

    @abstractmethod
    def notify_changes(self):
        raise NotImplementedError("Subclasses must implement the notify_changes() method.")


class Mediator(AbstractMediator):

    def __init__(self):
        super().__init__()
        self.recipe = recipe.Recipe(self)
        self.meal = meal.Meal(self)
        self.daily_meal_plan = daily_meal_plan.DailyMealPlan(self)
        self.meal_plan = meal_plan.MealPlan(self)
        self.ui = user_interface.UserInterface(self)

    def notify_changes(self):
        pass