#!/usr/bin/python3
"""Defines unittests for city class"""

import models
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_id_is_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)


if __name__ == "__main__":
    unittest.main()
