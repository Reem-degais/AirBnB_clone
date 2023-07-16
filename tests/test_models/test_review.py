#!/usr/bin/python3
"""Defines unittests for review class"""

import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing Review class"""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)


if __name__ == "__main__":
    unittest.main()
