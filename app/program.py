# /usr/bin/env
"""module to start The Agile Planner app by defining the main function
This app was written using Python version 3.5.2
This version of the app is implementing the Mediator design pattern"""

from app.ui import user
from app.recipe import recipe_facade


def main():
    #  Singleton implementation: assert only one instance of User is created due to Singleton pattern on User
    #  See app.ui.user for class implementation of Singleton
    user1 = user.User('Taylor')
    user2 = user.User('Brett')
    assert user1 is user2
    print('No AssertionError thrown, second user never created as both user variables are set to Taylor: ')
    print('User1 variable name: ' + str(user1.name))
    print('User2 variable name: ' + str(user2.name))

    # Facade implementation
    recipe_facade_obj = recipe_facade.RecipeFacade()

    # Adapter implementation

    # Factory implementation


if __name__ == '__main__':
    main()
