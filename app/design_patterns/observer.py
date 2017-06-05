"""observer module for implementation of observer design pattern"""
from abc import ABC, abstractmethod
from app.meal_plan import meal, meal_plan


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class AbstractNotifyObservers(ABC):
    @abstractmethod
    def notify_observers(self):
        pass


class NotifyObservers(AbstractNotifyObservers):
    def __init__(self):
        pass

    def notify_observers(self):
        pass
