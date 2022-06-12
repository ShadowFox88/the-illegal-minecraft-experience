from registry.registry import ITEM_REGISTRY, CRAFTING_REGISTRY
from game.player import Player

from typing import List


class Recipe:
    """__init__ arguments:
        recipe_name - item_id for recipe registration
        result - result: (item_id, count)
        *materials - each arg should be formatted like this: (item_id, count)
    """
    
    def __init__(self, recipe_name, result : tuple, *materials : List[tuple]):
        self.recipe_list : List[tuple] = materials
        self.item_id = recipe_name

        self.result_id : tuple = result

        self.result_item = ITEM_REGISTRY.view_entry(self.result_id[0])

        for obj_id, obj_count in self.recipe_list:
            if ITEM_REGISTRY.view_entry(obj_id) == -2:
                print("Invalid crafting recipe(item in recipe doesn't exist): ", obj_id)

                exit(-2)

        if self.result_item == -2:
            print("Invalid crafting recipe result.")

            exit(-2)

    def craft(self, player: Player):
        for item, count in self.recipe_list:
            if player.inventory.get_item_count(item) >= count:
                pass
            else:
                return "Not enough items"

        for item, count in self.recipe_list:
            player.inventory.expend_item(item, count)

        player.inventory.gain_item(self.result_id[0], self.result_id[1])

    def craft_multiple(self, player: Player, count: int):
        output = None
        
        for i in range(count):
            output = self.craft(player)

            if output == "Not enough items":
                return output
                
                break

    def json(self):
        return {
            "recipe":self.recipe_list,
            "item_id":self.item_id 
        }

def register():
    CRAFTING_REGISTRY.register_entries(
        Recipe("planks1", ("oak_planks", 4), ("oak_wood", 1))
    )
