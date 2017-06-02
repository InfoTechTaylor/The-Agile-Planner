"""User module for classes and methods related to user, ensure that user only has one instance 
by importing singleton. Implement singleton.Singleton as metaclass for User """

from app.design_patterns import singleton


class User(metaclass=singleton.Singleton):  # User is an instance of Singleton due to use of metaclass

    def __init__(self, name):
        self.name = name
