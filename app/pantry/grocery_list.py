'''grocery list module'''
from app.design_patterns import singleton


class GroceryList(metaclass=singleton.Singleton):
    def __init__(self):
        self.grocery_list = []