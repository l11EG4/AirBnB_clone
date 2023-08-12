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
        """Command quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        """ Empty line and do nothing."""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_inst = eval(arg)()
                new_inst.save()
                print(new_inst.id)
            except NameError:
                print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
