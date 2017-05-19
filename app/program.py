"""module to start The Agile Planner app by defining the main function"""
from app import user_interface


def main():
    ui = user_interface.UserInterface()
    ui.print_banner(staticmethod)
    ui.print_menu(staticmethod)
    ui.get_user_choice()

if __name__ == '__main__':
    main()
