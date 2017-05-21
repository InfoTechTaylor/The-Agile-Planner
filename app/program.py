"""module to start The Agile Planner app by defining the main function"""
from app.ui import user_interface


def main():
    ui = user_interface.UserInterface()
    ui.print_banner()
    ui.print_main_menu()
    user_choice = ui.get_user_choice()
    ui.start_user_choice(user_choice)

if __name__ == '__main__':
    main()
