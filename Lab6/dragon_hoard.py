def add_to_inventory(inventory:dict, added_items: list) -> dict:
    updated_inventory = inventory.copy()
    for item in added_items:
        updated_inventory.setdefault(item, 0)
        updated_inventory[item] += 1
    return updated_inventory




if __name__ == "__main__":
    from fantasy_game_inventory import display_inventory
    inv = {"gold coin": 42, "rope": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    updated_inv = add_to_inventory(inv, dragon_loot)
    print(display_inventory(updated_inv))