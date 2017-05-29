"""adapter classes for the UserInterfaace class"""

from abc import ABC, abstractmethod
from app.ui import user_interface


class AbstractUIAdapter(ABC):
    def __init__(self):
        self._adaptee_ui = user_interface.UserInterface()

    @abstractmethod
    def display_banner(self):
        raise NotImplementedError('Subclasses must implement display_options()')

    @abstractmethod
    def display_recipe(self, recipe_obj):
        raise NotImplementedError('Subclasses must implement display_recipe()')


class UIAdapter(AbstractUIAdapter):
    def display_banner(self):
        self._adaptee_ui.print_welcome_banner()

    def display_recipe(self, recipe_obj):
        self._adaptee_ui.print_recipe(recipe_obj)
