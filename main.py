import registry.registry as Registry
import registry.crafting as Recipes

Registry.init()
Recipes.register()

print(Registry.ITEM_REGISTRY.view_all_entries())
