"""module to hold iterator design pattern classes"""

import collections.abc


class AbstractIterator(collections.abc.Iterable):
    def first(self):  # points to first element of collection
        pass

    def __next__(self):  # increments to the next element of the collection
        pass

    def is_done(self):  # true if iterator points past the last element of collection
        pass

    def current_item(self):  # return the element pointed to by the iterator
        pass


class RecipeBoxIterator(AbstractIterator):
    def __init__(self, recipe_obj_list):
        self._recipe_obj_list = recipe_obj_list

    def first(self):
        pass

    def __next__(self):
        pass

    def is_done(self):
        pass

    def current_item(self):
        pass