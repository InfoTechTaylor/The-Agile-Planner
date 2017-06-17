"""module for nutrition based classes and methods"""
from app.meal_plan import meal


class Nutrition:

    def calculate_calories(self, food_obj):
        total_calories = 0

        if isinstance(food_obj, meal.Meal):
            for recipe in food_obj.list:
                total_calories += recipe.calories
        else:
            for meal_obj in food_obj.list:
                if meal_obj is None:
                    pass
                else:
                    total_calories += meal_obj.total_calories

        food_obj.total_calories = total_calories

        return total_calories
