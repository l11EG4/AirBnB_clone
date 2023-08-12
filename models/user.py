#!/usr/bin/python3
"""Defines User class that inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a user class.

    Args:
        email(str): email of user.
        password(str): password of user.
        first_name(str): first name of user.
        last_name(str): last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
