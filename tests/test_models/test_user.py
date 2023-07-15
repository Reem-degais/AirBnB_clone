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

if __name__ == "__main__":
    unittest.main()
