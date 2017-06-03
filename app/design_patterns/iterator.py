"""module to hold iterator design pattern classes"""

import collections.abc


class AbstractIterator(collections.abc.Iterable):
    def first(self):  # points to first element of collection
        pass

    def __iter__(self):
        pass

    def __next__(self):  # increments to the next element of the collection
        pass

    def is_done(self):  # true if iterator points past the last element of collection
        pass

    def current_item(self):  # return the element pointed to by the iterator
        pass


class RecipeBoxIterator(AbstractIterator):
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.value:
            index = self.index
            self.index += 1
            return index
        else:
            raise StopIteration()

    def first(self):
        pass

    def is_done(self):
        pass

    def current_item(self):
        pass