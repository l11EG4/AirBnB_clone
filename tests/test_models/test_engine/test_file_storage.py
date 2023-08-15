#!/usr/bin/python3
"""Defines an unittest for  FileStorage class."""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests to test FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method_returns_dictionary(self):
        instances_dict = self.storage.all()
        self.assertIsInstance(instances_dict, dict)

    def test_new_method_adds_object_to_objects(self):
        instance = BaseModel()
        self.storage.new(instance)
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_method_saves_to_json_file(self):
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()

        with open("file.json", "r") as file:
            data = json.load(file)
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            self.assertIn(key, data)

    def test_reload_method_loads_objects_from_json_file(self):
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, new_storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
