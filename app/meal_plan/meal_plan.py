"""meal plan module for MealPlan and DailyMealPlan classes"""


class DailyMealPlan:

    def __init__(self, day_of_week):
        self.day_of_week = day_of_week
        self.total_calories = 0
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        self.list = [self.breakfast, self.lunch, self.dinner]

    def add_meal(self, meal_obj):

        if meal_obj.meal_type == 'Breakfast':
            self.breakfast = meal_obj
            self.list[0] = self.breakfast
        elif meal_obj.meal_type == 'Lunch':
            self.lunch = meal_obj
            self.list[1] = self.lunch
        elif meal_obj.meal_type == 'Dinner':
            self.dinner = meal_obj
            self.list[2] = self.dinner

        return self


class MealPlan:

    def __init__(self, start_date):
        self.start_date = start_date
        self.list = []  # list of DailyMealPlan() objects
        self.total_calories = 0

    def add_daily_meal_plan(self, daily_meal_plan):
        self.list.append(daily_meal_plan)

        return self
