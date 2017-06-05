"""Command design pattern module"""

from abc import ABC, abstractmethod


class Invoker:
    """stores commands until they are ready to execute, executes those commands"""
    def __init__(self):
        self._commands_list = []

    def add_command(self, command):
        self._commands_list.append(command)

    def execute_commands(self):
        for command in self._commands_list:
            command.execute_command()

    def undo_command(self, command):
        self._commands_list.remove(command)


class AbstractCommand(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute_command(self):
        pass


class AddRecipeToMealCommand(AbstractCommand):
    def __init__(self, meal_receiver, recipe_obj):
        super().__init__(meal_receiver)
        self.meal_receiver = self.receiver
        self.recipe_obj = recipe_obj

    def execute_command(self):
        self.meal_receiver.add_recipe(self.meal_receiver, self.recipe_obj)
