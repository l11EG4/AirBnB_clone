#!/usr/bin/python3
# Made by LAILA & MEGA
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
from models.user import User
import os


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_inheritance(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_defaults(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(str(self.user.id), user_dict['id'])

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(
            self.user.__class__.__name__, self.user.id, self.user.__dict__
        )
        self.assertEqual(str(self.user), expected_str)

if __name__ == '__main__':
    unittest.main()
