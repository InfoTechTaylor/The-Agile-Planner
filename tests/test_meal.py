'''test cases for the meal module'''

from app.meal_plan import meal

def test_meal_type_attribute():
    meal_obj = meal.Meal('Lunch')
    assert meal_obj.meal_type == 'Lunch'

def test_add_recipe():
    pass

def test_calculate_calories():
    pass
