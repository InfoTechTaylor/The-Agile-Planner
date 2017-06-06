"""Meal factory for determining which type of meal to create"""

from abc import ABC, abstractmethod
from app.meal_plan import meal


class AbstractMealFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_meal(self, meal_type, successor):
        raise NotImplementedError('Subclasses must implement create_meal()')


class MealFactory(AbstractMealFactory):
    def __init__(self):
        super().__init__()

    def create_meal(self, meal_type, successor):
        if meal_type == 'breakfast':
            return meal.Breakfast()
        elif meal_type == 'lunch':
            return meal.Lunch(successor)
        elif meal_type == 'dinner':
            return meal.Dinner()
