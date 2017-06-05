"""Command design pattern module"""

from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    def __init__(self):
        self.command_list = []

    @abstractmethod
    def add_command(self, command):
        pass

    @abstractmethod
    def undo_command(self, command):
        pass

    @abstractmethod
    def execute_commands(self):
        pass


class CreateNewRecipeCommand(AbstractCommand):
    def __init__(self):
        super().__init__()

    def add_command(self, command):
        self.command_list.append(command)

    def undo_command(self, command):
        self.command_list.remove(command)

    def execute_commands(self):
        for command in self.command_list:
            command.execute()
