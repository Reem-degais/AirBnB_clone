#!/usr/bin/python3
#!/usr/bin/python3
"""Defines unittests for user class"""

import models
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing User class"""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

     def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User.last_name))

if __name__ == "__main__":
    unittest.main()
