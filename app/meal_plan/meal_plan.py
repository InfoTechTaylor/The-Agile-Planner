"""meal plan module for MealPlan and DailyMealPlan classes"""

from app.design_patterns import observer


class MealPlan(observer.AbstractObserver):
    def update(self):
        pass


class DailyMealPlan(observer.AbstractObserver):
    def update(self):
        pass