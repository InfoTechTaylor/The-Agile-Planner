"""User module for classes and methods related to user, ensure that user only has one instance """


class Singleton(type):  # defining Singleton as a metaclass

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class User(metaclass=Singleton):  # User is an instance of Singleton due to use of metaclass

    def __init__(self, name):
        self.name = name
