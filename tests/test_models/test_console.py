#!/usr/bin/python3
""" Defines all unittests for console.py."""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing prompt."""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"count User")
            self.assertEqual("2", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"count Place")
            self.assertEqual("1", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"count NonExistentClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
