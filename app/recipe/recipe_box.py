"""recipe_box module for RecipeBox class"""


class RecipeBox:
    def __init__(self):
        pass

    def get_all_recipes(self):
        recipe_box_csv = open('recipe/recipe_box.csv', 'r')
        for row in recipe_box_csv:
            row = row.split(',')
            print('-------------------------------------------------------------------'),
            print('| Recipe: ' + row[0]),
            print('| Nutritional Info: '),
            print('|   Calories: ' + row[1])
            print('|   Fat: ' + row[2])
            print('|   Carbs: ' + row[3])
            print('|   Protein: ' + row[4])
            print('-------------------------------------------------------------------')
        recipe_box_csv.close()

    def browse_recipes(self):
        pass # TODO have recipe card objects set so user can cycle through recipes, not display all

