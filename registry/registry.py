from typing import Union, Any, Dict, List
from registry.item import Item

import registry.item_object as objects

import json

class Registry:
    RegItem = Item
    
    def __init__(self, entry_type : Union[Any]):
        self.entry_type : Union[Any] = entry_type
        self.registry : Dict[self.entry_type] = {}

    def register_entry(self, object):
        if not isinstance(object, self.entry_type):
            return -1

        if not self.registry.__contains__(object):
            self.registry[object.item_id] = object
        else:
            return -2

    def delete_registry(self, object):
        if isinstance(object, self.entry_type):
            return -1

        if self.registry.__contains__(object):
            self.registry.pop(object.item_id)
        else:
            return -2

    def register_entries(self, *objects):
        for object in objects:
            self.register_entry(object)

    def view_entry(self, object_id : str):
        if self.registry.__contains__(object):
            return self.registry[object_id]
        else:
            return -2

    def view_all_entries(self):
        return_dict = {}
        for key, item in self.registry.items():
            return_dict[key] = item.json()

        return return_dict

    def __repr__(self):
        return self.registry

ITEM_REGISTRY = Registry(Registry.RegItem)
CRAFTING_REGISTRY = Registry(object)

def init():
    for key, obj in objects.__dict__.items():
        ITEM_REGISTRY.register_entry(obj)
    