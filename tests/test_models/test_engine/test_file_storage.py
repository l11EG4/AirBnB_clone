#!/usr/bin/python3
# Made by LAILA & MEGA
"""Defines unittests for models/engine/file_storage.py.

Unittest classes
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage

    def test_attributes(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        user = User()
        self.storage.new(user)
        all_objects = self.storage.all()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in all_objects)

    def test_save_reload(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in all_objects)

    def test_reload_nonexistent_file(self):
        # Test reload when the file does not exist
        nonexistent_storage = FileStorage()
        nonexistent_storage.reload()
        self.assertEqual(nonexistent_storage.all(), {})

if __name__ == '__main__':
    unittest.main()
