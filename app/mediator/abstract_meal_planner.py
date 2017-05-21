from abc import ABC, abstractmethod # ABC = Abstract Base Class, for defining abstract classes


class AbstractMealPlanner(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update_recipe(self):
        raise NotImplementedError("Subclasses must implement the update_recipe() method.")