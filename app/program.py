# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2"""

from app.ui import user_interface
from app.mediator import mediator_classes


def main():
    mediator_obj = mediator_classes.Mediator()

    ui = user_interface.UserInterface(mediator_obj)
    ui.print_banner()
    ui.print_main_menu()
    user_choice = ui.get_user_choice()
    ui.start_user_choice(user_choice)

if __name__ == '__main__':
    main()
