#!/usr/bin/python3
"""Defines unittests for basemodel class"""

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test case for the BaseModel class.

    This test case verifies the behavior and correctness of the BaseModel
    class methods.

    Test methods:
    - test_attributes: Ensures that the BaseModel instance has the expected
    attributes and their types.
    - test_str_method: Verifies that the __str__ method of the BaseModel
    class returns the expected string representation.
    - test_save_method: Checks that the save method of the BaseModel class
    updates the 'updated_at' attribute.
    - test_to_dict_method: Validates the correctness of the to_dict method
    of the BaseModel class.
    """

    def test_attributes(self):
        """
        Test the attributes of the BaseModel instance.

        This test verifies that the BaseModel instance has the expected
        attributes and their types.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertIsInstance(model.id, str)
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertIsInstance(model.created_at, datetime)
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel instance.

        This test checks that the __str__ method of the BaseModel class
        returns the expected string representation.
        """
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)

    def test_save_method(self):
        """
        Test the save method of the BaseModel instance.

        This test ensures that the save method of the BaseModel class
        updates the 'updated_at' attribute.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel instance.

        This test validates the correctness of the to_dict method of the
        BaseModel class,
        including the presence and correctness of various attributes in
        the returned dictionary.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertIn('created_at', model_dict)
        self.assertEqual(
                model_dict['created_at'], model.created_at.isoformat()
                )
        self.assertIn('updated_at', model_dict)
        self.assertEqual(
                model_dict['updated_at'], model.updated_at.isoformat()
                )

    def test_attribute_assignment(self):
        """
        Test assigning and retrieving attributes of the BaseModel instance.

        This test verifies that attributes can be assigned to the BaseModel
        instance and retrieved with the expected values.
        """
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        self.assertEqual(model.name, "My First Model")
        self.assertEqual(model.my_number, 89)

    def test_attribute_modification(self):
        """
        Test modifying attributes of the BaseModel instance.

        This test verifies that attributes of the BaseModel instance
        can be modified and the changes are reflected correctly.
        """
        model = BaseModel()
        model.name = "Original Model"
        model.my_number = 42
        model.name = "Updated Model"
        model.my_number = 100
        self.assertEqual(model.name, "Updated Model")
        self.assertEqual(model.my_number, 100)

    def teat_json_serialization(self):
        """
        Test converting the BaseModel instance to JSON and loading from JSON.

        This test ensures that the BaseModel instance can be successfully
        converted to JSON and the JSON representation can be loaded into
        a new instance with the same attributes.
        """
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        model_json = model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.my_number, model.my_number)
        self.assertEqual(new_model.created_at, model.created_aat)
        self.assertEqual(new_model.updated_at, model.updated_at)

    def test_unique_id(self):
        """
        Test the uniqueness of the 'id' attribute.

        This test ensures that each instance of the BaseModel class has
        a unique 'id' value.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """
        Test the type of the 'created_at' attribute.

        This test ensures that the 'created_at' attribute is of type
        'datetime'.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
