#!/usr/bin/python3
"""
base class
"""


import json


class Base:
    """base clase"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initial attributes"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and len(list_dictionaries):
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        tmp = []
        if list_objs:
            for items in list_objs:
                tmp.append(items.to_dictionary())

        info = cls.to_json_string(tmp)
        with open(str(cls.__name__) + ".json", "w") as new_file:
            new_file.write(info)
