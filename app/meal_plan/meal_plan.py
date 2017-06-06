"""meal plan module for MealPlan and DailyMealPlan classes"""

from app.design_patterns import chain_of_responsibility
from app.meal_plan import meal


class DailyMealPlan(chain_of_responsibility.AbstractHandler):

    def __init__(self, successor):
        super().__init__(successor)
        self.breakfast = meal.Breakfast()
        self.lunch = meal.Lunch(successor)
        self.dinner = meal.Dinner()
        self.total_calories = 0

    def add_meal(self, meal_obj):

        if meal_obj.meal_type == 'Breakfast':
            self.breakfast = meal_obj
        elif meal_obj.meal_type == 'Lunch':
            self.lunch = meal_obj
        elif meal_obj.meal_type == 'Dinner':
            self.dinner = meal_obj

    def calculate_calories(self):
        self.total_calories = self.breakfast.total_calories + self.lunch.total_calories + self.dinner.total_calories
        return self.total_calories

    def handle_request(self):
        self.calculate_calories()
        self.successor.handle_request()


class MealPlan(chain_of_responsibility.AbstractHandler):

    def __init__(self, successor):
        super().__init__(successor)
        self.daily_meal_plan_list = []
        # self.sunday = DailyMealPlan()

        self.total_calories = 0

    def add_daily_meal_plan(self, daily_meal_plan):
        self.daily_meal_plan_list.append(daily_meal_plan)

    def calculate_calories(self):
        for meal_plan in self.daily_meal_plan_list:
            self.total_calories += meal_plan.total_calories

        return self.total_calories

    def handle_request(self):
        if self.successor is not None:
            self.calculate_calories()
            self.successor.handle_request()
