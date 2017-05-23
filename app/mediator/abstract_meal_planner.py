from abc import ABC, abstractmethod # ABC = Abstract Base Class, for defining abstract classes


class AbstractMealPlanner(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def update_calories(self, recipe_name, updated_calories):
        raise NotImplementedError("Subclasses must implement the update_calories() method.")
