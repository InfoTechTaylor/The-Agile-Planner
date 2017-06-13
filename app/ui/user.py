"""User module for classes and methods related to user, ensure that user only has one instance 
by importing singleton. Implement singleton.Singleton as metaclass for User """

from app.design_patterns import singleton


class User(metaclass=singleton.Singleton):  # User is an instance of Singleton due to use of metaclass

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.daily_calorie_goal = None
        self.daily_carb_goal = None
        self.daily_fat_goal = None
        self.daily_protein_goal = None

    def set_daily_calorie_goal(self, daily_calorie_goal):
        self.daily_calorie_goal = daily_calorie_goal

    def set_daily_carb_goal(self, daily_carb_goal):
        self.daily_carb_goal = daily_carb_goal

    def set_daily_fat_goal(self, daily_fat_goal):
        self.daily_fat_goal = daily_fat_goal

    def set_daily_protein_goal(self, daily_protein_goal):
        self.daily_protein_goal = daily_protein_goal
