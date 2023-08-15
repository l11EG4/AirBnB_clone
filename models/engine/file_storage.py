#!/usr/bin/python3
""" Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Serialize instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """ Sets in __Objects the obj with key<obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serealizes __objects to JSON file."""
        obj_dict = {}

        for key, value in self.__objects.items():
            """if type(obj) is dict:
            obj_dict[key] = value
            else:"""
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    if class_name == "BaseModel":
                        self.new(BaseModel(**value))
                    elif class_name == "User":
                        self.new(User(**value))
                    elif class_name == "Place":
                        self.new(Place(**value))
                    elif class_name == "State":
                        self.new(State(**value))
                    elif class_name == "City":
                        self.new(City(**value))
                    elif class_name == "Amenity":
                        self.new(Amenity(**value))
                    elif class_name == "Review":
                        self.new(Review(**value))
        except FileNotFoundError:
            return
