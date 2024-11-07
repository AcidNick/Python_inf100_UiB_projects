def display_inventory(inventory: dict) -> str:
    inventory_str = 'Inventory:\n'
    for key, value in inventory.items():
        inventory_str += f'{value} {key}\n'
    total_items = sum(inventory.values())
    inventory_str += f'\nTotal number of items: {total_items}'
    return inventory_str


if __name__ == '__main__':
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    print(display_inventory(stuff))