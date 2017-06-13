"""meal plan module for MealPlan and DailyMealPlan classes"""

from app.meal_plan import meal


class DailyMealPlan():

    def __init__(self, day_of_week):
        self.day_of_week = day_of_week
        self.breakfast = meal.Breakfast()
        self.lunch = meal.Lunch()
        self.dinner = meal.Dinner()
        self.total_calories = 0

    def add_meal(self, meal_obj):

        if meal_obj.meal_type == 'Breakfast':
            self.breakfast = meal_obj
        elif meal_obj.meal_type == 'Lunch':
            self.lunch = meal_obj
        elif meal_obj.meal_type == 'Dinner':
            self.dinner = meal_obj

        return self

    def calculate_calories(self):
        self.total_calories = self.breakfast.total_calories + self.lunch.total_calories + self.dinner.total_calories
        return self.total_calories


class MealPlan():

    def __init__(self, start_date):
        self.start_date = start_date
        self.daily_meal_plan_list = []
        self.total_calories = 0

    def add_daily_meal_plan(self, daily_meal_plan):
        self.daily_meal_plan_list.append(daily_meal_plan)

        return self

    def calculate_calories(self):
        for meal_plan in self.daily_meal_plan_list:
            self.total_calories += meal_plan.total_calories

        return self.total_calories
