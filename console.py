#!/usr/bin/python3
"""Defines the entry point of the command interpreter."""
import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command Quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        """ Empty line and do nothing."""
        pass

    def do_create(self, arg):
        """ Creates a new inctance of BaseModel."""
        arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
