import unittest
from ..app import user


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = user.User()

    def test_create_user(self):
        pass
