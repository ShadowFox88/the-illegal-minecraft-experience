import registry.registry as Registry
import registry.crafting as Recipes
import game.player as Player

Registry.init()

print(Registry.ITEM_REGISTRY.view_all_entries())

Recipes.register()

player = Player.Player()

player.inventory.gain_item("oak_planks", 3)
player.inventory.gain_item("stick", 2)
player.craft_item("pickaxe1")

print(player.inventory.get_item_count("oak_planks"))
print(player.inventory.get_item_count("oak_wood"))
print(player.inventory.get_item_count("wooden_pickaxe"))
