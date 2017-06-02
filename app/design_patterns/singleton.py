"""module for singleton class for the purpose of reuse by multiple packages/classes"""


class Singleton(type):  # defining Singleton as a metaclass

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
