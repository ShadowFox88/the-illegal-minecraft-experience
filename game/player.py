import registry.registry as registry

class Player:
    def __init__(self):
        self.inventory = self.Inventory()
        self.health = 20

    class Inventory:
        def __init__(self):
            self.internal_inventory = {}

        def set_item(self, item_id : str, count : int):
            if registry.ITEM_REGISTRY.view_entry(item_id) == -2:
                return "This item doesn't exist"
            else:
                self.internal_inventory[item_id] = count
        
        def expend_item(self, item_id : str, count : int):
            if registry.ITEM_REGISTRY.view_entry(item_id) == -2:
                return "This item doesn't exist"
            else:
                try:
                    curr_item_count = self.internal_inventory[item_id]
                except KeyError:
                    self.set_item(item_id, 0)
                    
                    return "Not enough items."
                
                if curr_item_count - count >= 0:
                    self.internal_inventory[item_id] -= count
                else:
                    return "Not enough items"

        def gain_item(self, item_id : str, count : int):
            if registry.ITEM_REGISTRY.view_entry(item_id) == -2:
                return "This item doesn't exist"
            else:
                if self.internal_inventory.__contains__(item_id):
                    self.internal_inventory[item_id] += count
                else:
                    self.internal_inventory[item_id] = count

        def get_item_count(self, item_id : str):
            if registry.ITEM_REGISTRY.view_entry(item_id) == -2:
                return "This item doesn't exist"
            else:
                if self.internal_inventory.__contains__(item_id):
                    return self.internal_inventory[item_id]
                else:
                    return 0

    def lose_health(self, health : int):
        self.health -= health

    def gain_health(self, health : int):
        self.health += health

    def craft_item(self, recipe_id : str):
        recipe = registry.CRAFTING_REGISTRY.view_entry(recipe_id)

        if recipe != -2:
           result = recipe.craft(self)
        
        if result == "Not enough items":
            print("Couldn't craft.")
