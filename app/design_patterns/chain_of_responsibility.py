"""chain of responsiblity module for implementation of chain of responsibility design pattern"""
from abc import ABC, abstractmethod


class AbstractHandler(ABC):

    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self):
        pass
